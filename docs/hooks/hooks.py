from os.path import relpath
from functools import partial
import re


def on_config(config):
    config.tags_paths = dict()
    return config


def on_page_markdown(markdown, page, config,  **kwargs):
    tag_ids = re.findall(r'@tag\((.+?)\)', markdown)
    config.tags_paths.update({k: page.url for k in tag_ids})
    span = r'<span id="\1"></span>'
    markdown = re.sub(r'(?<!-)@tag\((.+?)\)', span, markdown)
    return re.sub(r'-@tag\((.+?)\)', r'@tag(\1)', markdown)


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
    rel_tr = partial(transform, config.tags_paths, page.url)

    def on_match(m):
        return f'<a href="{rel_tr(m.group(1))}">'

    return re.sub('<a href="(.+?)">', on_match, html)
