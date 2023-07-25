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


def load_navigation():
	"""Load Mkdocs navigation object

	"""
	config = load_config(s.path_cfg_file)
	files = load_files()
	nav_object = get_navigation(files, config)
	for p in nav_object.pages:
		p.read_source(config)
	return nav_object


def is_adm_line(line):
	return line.startswith(("??? ", "!!! "))


def _update_ref_dict(page, ref_dict):
	if page.markdown is not None:
		for line in page.markdown.split('\n'):
			if is_adm_line(line):
				if " id=" in line:
					line = " ".join(line.split())
					identifier = line.split(" id=")[1]
					ref_dict.update({identifier: page.url})


def get_ref_dict(url=None):
	nav_object = load_navigation()
	ref_dict = dict()
	for page in nav_object.pages:
		_update_ref_dict(page, ref_dict)
	if url is not None:
		return get_rel_dict(ref_dict, url)
	else:
		return ref_dict


def get_rel_dict(ref_dict, url):
	return {k: relpath(v, url) for k, v in ref_dict.items()}


def update_references(text, url, ref_dict=None):
	if ref_dict is None:
		rel_dict = get_ref_dict(url)
	else:
		rel_dict = get_rel_dict(ref_dict, url)
	rel_links = {key: f'{path}/#{key}' for key, path in rel_dict.items()}
	replacements = {f'@ref({tag})': f'<a href="{link}"><b>link</b></a>' for tag, link in rel_links.items()}
	for k, v in replacements.items():
		text = text.replace(k, v)
	return text
