# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'pimpmyplot'
copyright = '2024, clarkmaio'
author = 'clarkmaio'
release = '0.1.0' # Will be parsed from setup.py ideally, but let's keep it simple

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',    # Supports both numpy and google docstrings
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_logo = "../assets/pimpmyplotlogo.png"

html_theme_options = {
    "logo": {
        "text": "pimpmyplot",
        "link": "index",
    },
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/clarkmaio/pimpmyplot",
            "icon": "fa-brands fa-github",
        },
    ],
    "show_toc_level": 2,
    "navigation_depth": 4,
}

autosummary_generate = True
