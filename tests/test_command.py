from click.testing import CliRunner
from mkdocs import __main__ as cli
from unittest import mock

runner = CliRunner()


@mock.patch('mkdocs.commands.serve.serve', autospec=True)
def test_serve_default(mock_serve):
    result = runner.invoke(cli.cli, ["serve"], catch_exceptions=False)
    assert True
