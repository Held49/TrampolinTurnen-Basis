# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

#project = 'Einführung ins Trampolinturnen'
project = 'Trampolinturnen'
copyright = '2022, Ingmar Splitt'
author = 'Ingmar Splitt'
release = '0.2'  # TODO: change to date
builder = "html latexpdf"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'de'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'
html_static_path = ['_static']

# -- Options for LATEX output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/latex.html

latex_elements = {
    "papersize": "a4paper",
    "pointsize": "14pt",
    "fncychap": '',  # '\\usepackage[Bjornstrup]{fncychap}',
    "transition": "\\bigskip"
}
