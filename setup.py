import os
import setuptools

name = 'landbosse'
version = '2.1.5'

with open('README.md', 'r') as fh:
    long_description = fh.read()

PACKAGE_PATH = os.path.abspath(os.path.join(__file__, os.pardir))

setuptools.setup(
    url='https://github.com/WISDEM/LandBOSSE',
    name=name,
    version=version,
    author='NREL',
    author_email='alicia.key@nrel.gov',
    description='LandBOSSE',
    long_description=long_description,
    long_description_content_type='text/markdown',
    #packages=['landbosse'],
    packages=setuptools.find_packages(PACKAGE_PATH, "test"),
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=[
        'pandas',
        'numpy',
        'sympy',
        'scipy',
        'shapely',
        'xlsxwriter',
        'xlrd'
    ],
    command_options={
            'build_sphinx': {
                'project': ('setup.py', name),
                'version': ('setup.py', version),
                # 'release': ('setup.py', release),  # Not yet needed
                'source_dir': ('setup.py', 'docs')}}
)
