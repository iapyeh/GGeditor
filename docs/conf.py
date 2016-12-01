import sys, os

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

sys.path.append(os.path.abspath(os.pardir))
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..','backend'))

__version__ = '1.0'

# -- General configuration -----------------------------------------------------
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
source_suffix = '.rst'
master_doc = 'index'
project = 'GGEditor'
copyright = '2016, Yeh Hsin Yuan'

# -- Options for HTML output ---------------------------------------------------

html_theme = 'default'

html_static_path = ['static']
latex_documents = []

def run_apidoc(_):
    from sphinx.apidoc import main
    parentFolder = os.path.join(os.path.dirname(__file__), '..')
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(parentFolder)
    module = os.path.join(parentFolder,'backend')
    output_path = os.path.join(cur_dir, 'api')
    main(['-e','-f','-o', output_path, module])

def setup(app):
    # overrides for wide tables in RTD theme
    app.add_stylesheet('theme_overrides.css')   # path relative to _static
    app.connect('builder-inited', run_apidoc)
