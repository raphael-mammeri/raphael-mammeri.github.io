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
					print(line)
					line = " ".join(line.split())
					identifier = line.split(" id=")[1]
					ref_dict.update({identifier: page.url})


def get_ref_dict(url=None):
	nav_object = load_navigation()
	ref_dict = dict()
	for page in nav_object.pages:
		_update_ref_dict(page, ref_dict)
	if url is not None:
		ref_dict.update({k: relpath(v, url) for k, v in ref_dict.items()})
	return ref_dict
