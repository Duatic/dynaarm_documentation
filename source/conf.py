# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DynaArm Documentation'
copyright = '2025, Duatic AG'
author = 'Duatic AG'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_copybutton",
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinx_rtd_theme",
    "myst_parser"
]

templates_path = ['_templates']
exclude_patterns = ['**/CONTRIBUTING.md', '**/README.md', '**/CHANGELOG.rst']

master_doc = "index"

source_suffix = ".rst"

# Automatically sets numbers to figures. Used for referencing figures properly.
numfig = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": -1,

}

html_context = {
    "display_github": True,
    "github_user": "Duatic",
    "github_repo": "dynaarm_documentation",
    "github_version": "main/",
    "conf_py_path": "/source/",
    "favicon": "logo.png",
    "logo": "logo.png"
}

html_favicon = "_static/logo_small.png"
html_logo = "_static/logo.png"

# -- Options for PDF output --------------------------------------------------------------------------------
#latex_engine = "xelatex"
latex_elements = {'fontenc' : r'\usepackage[LGR,T1]{fontenc}'}
latex_documents = [
  (master_doc, 'DynaArmDocumentation.tex', 'DynaArm Documentation',
   'Duatic AG', 'manual'),
]
latex_logo = "_static/logo_dark.png"

rst_prolog = """
.. warning::

   **Important Notice:** The DynaArm is currently a prototype and not ready for commercial use. It is intended solely for research and development purposes. Users are responsible for ensuring safe operation during its use.
"""