from os.path import relpath
from empty.utils import refactor_admonitions
from functools import partial
import re
from mkdocs.structure.nav import Navigation
from functools import reduce
def load_tagged_adm():
    return dict()


def on_config(config):
    config.tags_paths = dict()
    # Only \w are permitted in adm definition, thats ok but I think can be changed
    
    config.tagged_adms = dict()
    config.sources = dict()

    return config

def read_source(page):
    try:
        with open(page.file.abs_src_path, encoding='utf-8-sig', errors='strict') as f:
            source = f.read()
    except OSError:
        raise OSError(f'File not found: {page.file.src_path}')
    except ValueError:
        raise ValueError(f'Encoding error reading file: {page.file.src_path}')
    return source

def number(item):
    subitems = item.items if hasattr(item, "items") else item.children
    if subitems is not None:
        for k, subitem in enumerate(subitems):
            if subitem.title is not None:
                subitem.title = f"{k+1}. " + subitem.title
            if subitem.children is not None:
                number(subitem)

def cnumber(s):
    anc_numbers = []
    for a in s.ancestors:
        if hasattr(a, "number"):
            anc_numbers.append(a.number)
    anc_numbers.append(s.number)
    s.cnumber = ".".join(anc_numbers)
    if s.title is not None:
        s.title = " - ".join([s.cnumber, s.title])


def enumerate_children(element):
    if element.children is not None:
        for i, e in enumerate(element.children):
            e.number = str(i+1)
            cnumber(e)
            enumerate_children(e)

def on_nav(nav, config, files):
    for item in nav.items:
        enumerate_children(item)
    for page in nav.pages:
        source = read_source(page)
        tag_ids = re.findall(r'@tag\((.+?)\)', source)
        config.tags_paths.update({k: page.url for k in tag_ids})
        # next line is to prevent reading source twice
        # config.sources.update({page.file.src_path: source})
    return None


def on_page_read_source(page, config):
    try:
        # Only navigation sources read on nav
        source = config.sources[page.file.src_path]
    except KeyError:
        source = None
    return source


def on_page_markdown(markdown, page, config,  **kwargs):
    cnumber = page.cnumber if hasattr(page, "cnumber") else None
    markdown = refactor_admonitions(markdown, cnumber)
    span = r'<span id="\1"></span>'
    markdown = re.sub(r'(?<!-)@tag\((.+?)\)', span, markdown)
    return re.sub(r'-(@tag\(.+?\))', r'\1', markdown)


def transform(tags_paths: dict, url: str, tag_id: str):
    """Create the link to the referenced tag

    Create the relative path between url of page containing the reference
    and page containing the tag then add the tag to that relative path
    """
    if tag_id in tags_paths:
        rel_path = relpath(tags_paths[tag_id], url)
        r = f"{rel_path}/#{tag_id}"
        return f"{rel_path}/#{tag_id}"
    else:
        return tag_id


def on_page_content(html, page, config, **kwargs):
    rel_tr = partial(transform, config.tags_paths, page.url)

    def on_match(m):
        tag_id = m.group(1)
        return f'<a href="{rel_tr(tag_id)}">'
    new_html = re.sub('<a href="(.+?)">', on_match, html)
    if page.title == '2.2 - dev':
        print("hello")
    return re.sub('<a href="(.+?)">', on_match, html)

if __name__ == "__main__":
    from mkdocs.commands.serve import serve
    serve("/Users/mrm/Documents/Workspace/projects/raphael-mammeri/docs/mkdocs.yml")