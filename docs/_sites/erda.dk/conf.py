# Configuration file for the modi-helper-scripts documentation site.
# import sphinx_rtd_theme

from configparser import ConfigParser
import os
from types import SimpleNamespace

_SITE_DIR = os.path.dirname(os.path.abspath(__file__))


def _sitevars_and_epilog():
    parser = ConfigParser()
    parser.read(os.path.join(_SITE_DIR, "variables.ini"))

    sitevars = SimpleNamespace(**parser['site'])

    epilog_lines = [".. |%s| replace:: %s" % (k, v) for k, v in sitevars.__dict__.items()]
    epilog = '\n'.join(epilog_lines)

    return sitevars, epilog

# -- Project information -----------------------------------------------------

sitevars, rst_epilog = _sitevars_and_epilog()
project = "%s support" % (sitevars.project_name,)
copyright = "2023 SCIENCE HPC Center Support Team"
author = "SCIENCE HPC Center Support Team"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "sphinxemoji.sphinxemoji",
]
pygments_style = 'sphinx'
# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# HTML logo which will show on top of the sidebar
html_logo = "../../_static/faelles.svg"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["../../_static"]
html_css_files = ["custom.css"]
# Favicon for browsertab etcetera
html_favicon = '../../_static/favicon.ico'
