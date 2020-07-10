# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import sys
from pathlib import Path
import matplotlib
import recommonmark
from recommonmark.transform import AutoStructify
matplotlib.use('agg')

for f in Path(os.path.abspath('.')).joinpath('ibllib').rglob('__init__.py'):
    sys.path.insert(0, str(f.parent))

sys.path.append(os.path.join(os.path.dirname(__name__), '..'))


print('Python %s on %s' % (sys.version, sys.platform))
#print(sys.path)

# -- Project information -----------------------------------------------------

project = 'IBL Library'
copyright = '2018, International Brain Laboratory'
author = 'International Brain Laboratory'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.mathjax',
              'sphinx.ext.githubpages',
              'sphinx_copybutton',
              'nbsphinx',
              'myst_parser',
              'sphinx_material']
              #'sphinx_rtd_theme']
               #'recommonmark',

autosummary_generate = True
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# Only use nbsphinx for formatting the notebooks
nbsphinx_execute = 'never'
# Kernel to use for execution
nbsphinx_kernel_name = 'python3'
# Cancel compile on errors in notebooks
nbsphinx_allow_errors = True

nbsphinx_output_prompt = 'Out[%s]:'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_templates',
                    'documentation_contribution_guidelines.md', '.ipynb_checkpoints', 'templates',
                    '*colab*']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'default'
html_theme = 'sphinx_material'
#html_theme = 'sphinx_rtd_theme'


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['css/style.css']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ibllibdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'ibllib.tex', 'ibllib Documentation',
     'International Brain Laboratory', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'ibllib', 'ibllib Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ibllib', 'ibllib Documentation',
     author, 'ibllib', 'One line description of project.',
     'Miscellaneous'),
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
#source_suffix = ['.rst', '.md']
#source_parsers = {
#    '.md': 'recommonmark.parser.CommonMarkParser',
#}

plot_formats = [('png', 512)]



## Add extra thing at beginning of each ipynb
nbsphinx_prolog = r"""
{% set nb_name = env.doc2path(env.docname, base=None) | basename %}
{% set nb_path = env.doc2path(env.docname, base=None) | dirname %}
{% set colab_name = 'colab_' + nb_name %}

.. raw:: html
    
      <a href="{{ nb_name }}"><button id="download">Download tutorial notebook</button></a>
      <a href="https://github.com/mayofaulkner/ibllib/tree/master/docs/{{ nb_path }}/{{ nb_name }}"><button id="github">Github link</button></a>
      <a href="https://colab.research.google.com/github/mayofaulkner/ibllib/blob/gh-pages/{{ nb_path }}/{{ colab_name }}"><button id="colab">Colab link</button></a>

"""

#app setup hook if you want to use recommonmark by itself
#def setup(app):
#    app.add_config_value('recommonmark_config', {
#        #'url_resolver': lambda url: github_doc_root + url,
#        'auto_toc_tree_section': 'Contents',
#        'enable_math': False,
#        'enable_inline_math': False,
#        'enable_eval_rst': True,
#    }, True)
#    app.add_transform(AutoStructify)

