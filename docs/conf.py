import os
from recommonmark.parser import CommonMarkParser


def setup(app):
    app.add_stylesheet('my_theme.css')

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

todo_include_todos = True

master_doc = 'index'

project = u'Hardops'
copyright = u'2015, Hops'

version = '0.0.1'
release = '0.0.1'

exclude_patterns = ['includes/*']

pygments_style = 'sphinx'

htmlhelp_basename = 'Hardopsdoc'

latex_elements = {}
latex_documents = [
  ('index', 'Hardops.tex', u'Hardops Documentation',
   u'Hops', 'manual'),
]

man_pages = [
    ('index', 'Hardops', u'Hardops Documentation',
     [u'Hops'], 1)
]
texinfo_documents = [
  ('index', 'Hardops', u'Hardops Documentation',
   u'Hops', 'Hardops', 'A new way to work with data in Blender.',
   'Miscellaneous'),
]

epub_title = u'Hardops'
epub_author = u'Hops'
epub_publisher = u'Hops'
epub_copyright = u'2017, Hops'
epub_exclude_files = ['search.html']
