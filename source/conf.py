# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DynaArm Software Documentation'
copyright = '2024, Duatic AG'
author = 'Lennart Nachtigall'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_copybutton",
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinx_rtd_theme",
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


html_context = {
    "display_github": True,
    "github_user": "Duatic",
    "github_repo": "dynaarm_software_documentation",
    "github_version": "main/",
    "conf_py_path": "/source/",
    "favicon": "favicon.ico",
    "logo": "logo.png"
}

html_favicon = "_static/logo.png"
html_logo = "_static/logo.png"
