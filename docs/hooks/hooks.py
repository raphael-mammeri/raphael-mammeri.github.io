from empty.settings import Settings
from empty.plugin import page_url
from mkdocs.structure.nav import get_navigation
from mkdocs.structure.files import File, Files, get_files
from empty.utils import load_navigation
from os.path import relpath
from empty.utils import get_ref_dict
s = Settings()


def refactor_adm(line: str) -> str:
    """
    Transform admonition first line

    Expected syntax : !!! adm_name adm_title id=id_txt
    No extra quotes needed, id part must be last.
    """
    if line.startswith(("??? ", "!!! ")):
        # Remove extra white spaces
        line = " ".join(line.split())
        # split id part
        line = line.split(" id=")
        # split first part of admonition to get admonition type and title if any
        f = line[0].split()
        adm_sign = f[0] # !!!, ??? etc
        adm_name = f[1].capitalize() # admonition name
        # custom title given by user
        adm_title = f'({" ".join(f[2:])})' if len(f) > 2 else ""

        if len(line) == 2: # there is an identifier in this case
            identifier = line[1]
            title_name = f'<span id="{identifier}">{" ".join([adm_name, adm_title]).strip()}</span>'
        else:
            title_name = " ".join([adm_name, adm_title]).strip()
        return f'{adm_sign} {adm_name} "{title_name}"'
    else:
        return line


def update_references(markdown, url):
    rel_dict = get_ref_dict(url)
    rel_links = {key: f'{path}/#{key}' for key, path in rel_dict.items()}
    replacements = {f'@ref({tag})': f'<a href="{link}"><b>link</b></a>' for tag, link in rel_links.items()}
    for k, v in replacements.items():
        markdown = markdown.replace(k, v)
    return markdown


def on_page_markdown(markdown, page, **kwargs):
    lines = [refactor_adm(line) for line in markdown.split('\n')]
    markdown = "\n".join(lines)
    return update_references(markdown, page.url)
