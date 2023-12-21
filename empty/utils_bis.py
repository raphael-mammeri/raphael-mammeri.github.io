from empty.settings import Settings
from mkdocs.config.base import load_config
from pathlib import Path
from mkdocs.utils import meta
from empty.plugin import page_url
from mkdocs.structure.files import get_files
from mkdocs.structure.nav import get_navigation
import os


s = Settings()

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


def get_ref_dict():
	nav_object = load_navigation()
	ref_dict = dict()
	for page in nav_object.pages:
		_update_ref_dict(page, ref_dict)
	return ref_dict



adm_pattern = r'( *(!!!\+?|\?{3}\+?) *(\w+) *("(.*)")? *(@tag\((.+)\)){1}\n(\s{4}.+\n)+)'

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

def on_nav(nav, config, files):
    for item in nav.items:
        enumerate_children(item)
    for page in nav.pages:
        source = read_source(page)
        source, tagged_adm = refactor_tagged_adm(source, config.adm_pattern)
        config.sources.update({page.file.src_path: source})
        config.tagged_adms.update(tagged_adm)
    return None


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

    tag_ids = re.findall(r'@tag\((.+?)\)', markdown)
    config.tags_paths.update({k: page.url for k in tag_ids})
    
    span = r'<span id="\1"></span>'
    markdown = re.sub(r'(?<!-)@tag\((.+?)\)', span, markdown)
    return re.sub(r'-(@tag\(.+?\))', r'\1', markdown)