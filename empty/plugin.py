import mkdocs
from mkdocs.config import base, config_options as c

class MyPluginConfig(base.Config):
	enable = c.Type(bool, default=True)
	verbose = c.Type(bool, default=False)
	skip_checks = c.ListOfItems(c.Choice(('foo', 'bar', 'baz')), default=[])

class MyPlugin(mkdocs.plugins.BasePlugin[MyPluginConfig]):
	pass