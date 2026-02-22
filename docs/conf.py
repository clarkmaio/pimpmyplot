import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'pimpmyplot'
copyright = '2026, Andrea Maioli'
author = 'Andrea Maioli'
release = '0.0.5'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '../assets/pimpmyplotlogo.png'

# Execute the plotting script
import subprocess
try:
    print("Generating plots for documentation...")
    script_path = os.path.join(os.path.dirname(__file__), 'generate_plots.py')
    subprocess.check_call([sys.executable, script_path])
    print("Plots generated successfully.")
except Exception as e:
    print(f"Error generating plots: {e}")
