# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys, os

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

sys.path.append(os.path.abspath(os.pardir))

__version__ = '1.0'

# -- General configuration -----------------------------------------------------
#templates_path = ['_templates']
#extensions = ['sphinx.ext.autodoc', 'sphinx.ext.ifconfig', 'sphinx.ext.extlinks']
source_suffix = '.rst'
master_doc = 'index'
project = 'GGEditor'
copyright = '2016, Yeh Hsin Yuan'
#exclude_patterns = ['_build']
#release = __version__
#version = '.'.join(release.split('.')[:1])
#last_stable = '1.0.0'
#rst_prolog = '''
#
#.. |last_stable| replace:: :GGeditor-doc:`{0}`
#'''.format(last_stable)

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'

#extlinks = {
#    #'GGeditor-doc':  ('http://docs.GGeditor.com/%s/', '')
#}

# -- Options for HTML output ---------------------------------------------------

html_theme = 'default'
#if not on_rtd:
#    try:
#        import sphinx_rtd_theme
#        html_theme = 'sphinx_rtd_theme'
#        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
#    except ImportError:
#        pass

html_static_path = ['static']

"""
# Output file base name for HTML help builder.
htmlhelp_basename = 'GGeditordoc'

html_use_smartypants = True

# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
html_use_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

"""
def setup(app):
    # overrides for wide tables in RTD theme
    app.add_stylesheet('theme_overrides.css')   # path relative to _static

"""

# -- Options for LaTeX output --------------------------------------------------
latex_documents = [
    #('index', 'Chrolwer.tex', 'Chrolwer Documentation','Hsin Yuan Yeh','manual'),
]

# -- Options for manual page output --------------------------------------------
man_pages = [
    #('index', 'chrolwer', 'chrolwer documentation',
    # ['Hsin Yuan Yeh'], 1),
    #('chrolwer-themes', 'chrolwer-themes', 'A theme manager for Chrolwer',
    # ['Hsin Yuan Yeh'], 1),
    #('themes', 'chrolwer-theming', 'How to create themes for Chrolwer',
    # ['The Chrolwer contributors'], 1)
]
"""
