
import docspec
import pytest


@pytest.fixture
def module() -> docspec.Module:
  module = docspec.Module('a', None, None, [
    docspec.Class('foo', None, 'This is class foo.', None, None, None, [
      docspec.Data('val', None, None, 'int', '42'),
      docspec.Function('__init__', None, None, None, [
        docspec.Argument('self', docspec.Argument.Type.Positional, None, None, None)
      ], None, None),
    ]),
  ])
  module.sync_hierarchy()
  return module