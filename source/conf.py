# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os, sys
import pydata_sphinx_theme

# -- General configuration ------------------------------------------------

# sphinx extensions
extensions = [
#    "sphinx_design",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.youtube"
 ]

# source_suffix = ['.rst', '.md']
source_suffix = '.rst'
# The master toctree document.
master_doc = 'index'
# General information about the project.
project = 'Climate Dynamics Lab'
year = '2024'
author = 'Sebastian G. Mutz'
copyright = '{0}, {1}'.format(year, author)

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'zenburn'

#templates_path = ['.']

# -- Options for HTML output ----------------------------------------------

html_theme = "pydata_sphinx_theme"
html_logo = "img/CD_light.png"

html_theme_options = {
    "show_prev_next": False,
    "show_nav_level": 2,
    "logo": {
       "image_light": "img/CD_light.png",
       "image_dark": "img/CD_dark.png",
    },
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/Climate-Dynamics",
            "icon": "fa-brands fa-github",
        },
    ],
}

html_sidebars = {
    "index": [],  # Remove sidebars on landing page to save space
    "general": ["general/info.html"],
}

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are relative to html_static_path
html_css_files = ['css/style.css']


html_title = '%s' % (project)
