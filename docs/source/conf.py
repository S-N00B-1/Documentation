# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Legacy Edition Minigames'
copyright = '2023, Legacy Edition Minigames Contributors'
author = 'Legacy Edition Minigames Contributors'

release = '0.1'
version = '0.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_logo = "images/logo.png"
html_theme_options = {
    'logo_only': True,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Favicon
html_favicon = 'images/favicon.ico'
