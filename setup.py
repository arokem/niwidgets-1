"""Installer."""
from setuptools import setup
# To use a consistent encoding
from codecs import open
import os.path

here = os.path.dirname(os.path.abspath(__file__))
ver_file = os.path.join(here, 'niwidgets', 'version.py')

with open(ver_file) as f:
    exec(f.read(), globals(), locals())

version = locals()['__version__']

blurb = 'A package that provides ipywidgets for standard neuroimaging plotting'

readme = (open('README.md', 'r').read()
          if os.path.isfile('README.md')
          else blurb)

setup(
    name='niwidgets',
    version=version,
    description=blurb,
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/nipy/niwidgets',
    download_url='https://github.com/nipy/niwidgets/archive/' +
        version + '.tar.gz',
    # Author details
    author='Bjoern Soergel & Jan Freyberg',
    author_email='jan.freyberg@gmail.com',
    packages=['niwidgets'],
    keywords=['widgets', 'neuroimaging'],
    install_requires=['ipywidgets', 'nilearn', 'nibabel', 'ipyvolume'],
    # Include the template file
    package_data={
        '': ['data/*nii*',
             'data/*.trk',
             'data/examples_surfaces/lh.*',
             'data/examples_surfaces/*.ctab']
    },
)
