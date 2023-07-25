from empty.settings import Settings
from empty.plugin import page_url
from mkdocs.structure.nav import get_navigation
from mkdocs.structure.files import File, Files, get_files
from empty.utils import load_navigation
from os.path import relpath
from empty.utils import refactor_adm, update_references
from empty.utils import get_ref_dict
s = Settings()


def on_config(config):
    print("THIS IS CONFIG")
    config.ref_dict = get_ref_dict()
    return config


def on_files(files, config):
    print("THIS IS ON FILES")
    return files


def on_nav(nav, config, files):
    print("THIS IS NAVIGATION")
    for page in nav.pages:
        if page.markdown is None:
            print(f'This is a None markdown {page.url}')
    # config.ref_dict = get_ref_dict()
    return nav


def on_pre_build(config):
    print("THIS IS ON on_pre_build")


def on_post_build(config):
    print("THIS IS ON on_psot_build")


def on_env(env, config, files):
    print(f'THIS IS ON ENV')
    print(files.documentation_pages()[7].page.markdown)
    pass


def on_page_markdown(markdown, page, config,  **kwargs):
    print('THIS IS MARKDOWN')
    lines = [refactor_adm(line) for line in markdown.split('\n')]
    markdown = "\n".join(lines)
    return update_references(markdown, page.url, config.ref_dict)
