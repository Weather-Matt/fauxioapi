from setuptools import setup, find_packages, Extension
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name="fauxioapi",
    version="0.1.6",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.5',
    setup_requires=['numpy>=1.16,<=1.24.3','netCDF4>=1.2.9,<=1.5.8'],
    install_requires=['numpy>=1.16,<=1.24.3','netCDF4>=1.2.9,<=1.5.8'],
    scripts=['scripts/gen_grid_shape.py','scripts/regrid.py'],
    package_data={'fauxioapi': ['data/griddesc.txt']},
    url="https://github.com/jlbeidler/fauxioapi",
    author_email='james.beidler@gmail.com',
    description="A simple module reproducing limited I/O API functions",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
