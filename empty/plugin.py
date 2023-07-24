import mkdocs
from empty.settings import Settings
s = Settings()

from mkdocs.config import base, config_options as c

class MyPluginConfig(base.Config):
	enable = c.Type(bool, default=True)
	verbose = c.Type(bool, default=False)
	skip_checks = c.ListOfItems(c.Choice(('foo', 'bar', 'baz')), default=[])

def adm_dict():
	#file_path =
	pass

def page_url(page):
	return page.canonical_url



