from empty.settings import Settings
from mkdocs.config.base import load_config
from pathlib import Path
from mkdocs.utils import meta
from empty.plugin import page_url
from os.path import relpath
from mkdocs.structure.files import get_files
from mkdocs.structure.nav import get_navigation
import os

s = Settings()


def remove_extra_space(line):
	return " ".join(line.split())


def refactor_adm(line: str) -> str:
	"""
    Transform admonition first line

    Expected syntax : !!! adm_name adm_title id=id_txt
    No extra quotes needed, id part must be last.
    """

	if line.startswith(("???", "!!!")):
		# Remove extra white spaces
		line = " ".join(line.split())
		# split id part
		line = line.split(" id=")
		# split first part of admonition to get admonition type and title if any
		f = line[0].split()
		adm_sign = f[0]  # !!!, ??? etc
		adm_name = f[1].capitalize()  # admonition name
		# custom title given by user
		adm_title = f'({" ".join(f[2:])})' if len(f) > 2 else ""

		if len(line) == 2:  # there is an identifier in this case
			identifier = line[1]
			title_name = f'<span id="{identifier}">{" ".join([adm_name, adm_title]).strip()}</span>'
		else:
			title_name = " ".join([adm_name, adm_title]).strip()
		return f'{adm_sign} {adm_name} "{title_name}"'
	else:
		return line


def path_meta(path: Path) -> tuple:
	"""Extract content and meta infos from markdown

	Return tuple of content and dictionary of meta information.
	"""
	if os.path.isfile(path):
		with open(path) as f:
			text = "".joint(f.readlines())
		return meta.get_data(text)


def load_files():
	config = load_config(s.path_cfg_file)
	return get_files(config)


def is_adm_line(line):
	return line.startswith(("??? ", "!!! ", "???+ ", "!!!+ "))


def update_id_dict(id_dict, identifiers, url):
	id_dict.update({})


def update_ref_dict(markdown, url, ref_dict):
	for line in markdown.split('\n'):
		if is_adm_line(line):
			if " id=" in line:
				line = " ".join(line.split())
				identifier = line.split(" id=")[1]
				ref_dict.update({identifier: url})


def update_content(page, ref_dict=None):
	"""
	Replace references to id with  href links
	"""
	rel_dict = {k: relpath(path, page.url) for k, path in ref_dict.items()}
	rel_links = {k: f'{path}/#{k}' for k, path in rel_dict.items()}
	replacements = {f'@ref({tag})': f'<a href="{link}"><b>link</b></a>' for tag, link in rel_links.items()}
	if page.title == "functions":
		print(page.content)
	for k, v in replacements.items():
		page.content = page.content.replace(k, v)

def on_page_read_source(page, config):
    try:
        # Only navigation sources read on nav
        source = config.sources[page.file.src_path]
    except KeyError:
        source = None
    return source



