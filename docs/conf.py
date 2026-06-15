# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

import dotenv

sys.path.insert(0, os.path.abspath("../"))

from landscape_characterization import __version__

project = "Landscape Visualisation"
copyright = "2026, ColibriTD"
author = "ColibriTD"
release = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx_rtd_dark_mode",
    "sphinx_copybutton",
]
simplify_optional_unions = True
typehints_defaults = "comma"

dotenv.load_dotenv()
sphinx_github_changelog_token = os.getenv("SPHINX_GITHUB_CHANGELOG_TOKEN")
if sphinx_github_changelog_token is not None:
    extensions.append("sphinx_github_changelog")

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
