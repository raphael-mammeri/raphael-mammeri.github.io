from os.path import relpath
from functools import partial
from mkdocs.utils.meta import get_data
import re


def load_tagged_adm():
    return dict()


def on_config(config):
    config.tags_paths = dict()
    # Only \w are permitted in adm definition, thats ok but I think can be changed
    config.adm_pattern = r'( *(!!!\+?|\?{3}\+?) *(\w+) *("(.+)")? *(@tag\((.+)\)){1}\n(\s{4}.+\n)+)'
    config.tagged_adms = dict()
    config.sources = dict()

    return config


def adm_dict(adm_tuple):
    return {adm_tuple[6]: {
                "adm": adm_tuple[0],
                "name": adm_tuple[2],
                "title": adm_tuple[4],
                "tag": adm_tuple[5]}
    }


def refactor_tagged_adm(text: str, pattern):
    tagged_adm = dict()
    list_adm = re.findall(pattern, text)
    for adm_tuple in list_adm:
        tagged_adm.update(adm_dict(adm_tuple))

    def on_match(m):
        return "\n".join([m.group(6), m.group(0).replace(m.group(6), "")])
    text = re.sub(pattern, on_match, text)
    return text, tagged_adm


def read_source(page):
    try:
        with open(page.file.abs_src_path, encoding='utf-8-sig', errors='strict') as f:
            source = f.read()
    except OSError:
        raise OSError(f'File not found: {page.file.src_path}')
    except ValueError:
        raise ValueError(f'Encoding error reading file: {page.file.src_path}')
    return source


def on_nav(nav, config, files):
    print("This is on_nav")
    for page in nav.pages:
        source = read_source(page)
        source, tagged_adm = refactor_tagged_adm(source, config.adm_pattern)
        config.sources.update({page.file.src_path: source})
        config.tagged_adms.update(tagged_adm)
    return None


def on_page_read_source(page, config):
    print("This is page read source")
    try:
        # Only navigation sources read on nav
        source = config.sources[page.file.src_path]
    except KeyError:
        source = None
    return source


def on_page_markdown(markdown, page, config,  **kwargs):
    # add check that adm label is in adm dictionary


    def on_match(m):
        label = m.group(3)
        adm = config.tagged_adms[label]
        name = adm['name']
        new_line = m.group(0).replace(m.group(2), f'[{name}(1)]({label})')
        annotate = "{ .annotate }"
        first = "1."
        text = adm['adm']
        body = "\n".join(text.split("\n")[1:])
        body = "".join(["1.", body[2:]])
        return "\n".join([new_line, annotate, "", body])

    pattern = r"(.*(\[\]\((\w+)\)).*)"
    markdown = re.sub(pattern, on_match, markdown)
    if page.title == "1. Notations":
        print(markdown)
    tag_ids = re.findall(r'@tag\((.+?)\)', markdown)
    config.tags_paths.update({k: page.url for k in tag_ids})
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
        return f"{rel_path}/#{tag_id}"
    else:
        return tag_id


def on_page_content(html, page, config, **kwargs):
    if page.title == "3. Measure Theory Basics":
        #print(page.content)
        pass
    rel_tr = partial(transform, config.tags_paths, page.url)

    def on_match(m):
        return f'<a href="{rel_tr(m.group(1))}">'

    return re.sub('<a href="(.+?)">', on_match, html)
