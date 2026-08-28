# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Points autodoc at your source so it can import meteo_gis and pull
# docstrings straight from it. Matches the "src/" layout in pyproject.toml.
sys.path.insert(0, os.path.abspath('../src'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MeteoGIS'
copyright = '2026, David Duyile'
author = 'David Duyile'
release = '1.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',       # pulls docstrings from your code
    'sphinx.ext.napoleon',      # parses NumPy/Google-style docstrings (yours are NumPy-style)
    'sphinx.ext.viewcode',      # adds "view source" links next to each entry
    'sphinx.ext.intersphinx',   # links out to numpy/rasterio/geopandas docs where relevant
    'myst_parser',              # lets you write pages in Markdown, not just reStructuredText
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# Autodoc: show members in source order (not alphabetical), skip
# undocumented dunder methods, always include type hints inline.
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'member-order': 'bysource',
}
autodoc_typehints = 'description'

# Napoleon: your docstrings use NumPy style (Parameters / Returns /
# Raises sections), not Google style.
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = True
napoleon_use_rtype = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'rasterio': ('https://rasterio.readthedocs.io/en/stable/', None),
    'geopandas': ('https://geopandas.org/en/stable/', None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
