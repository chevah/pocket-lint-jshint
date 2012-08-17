from setuptools import setup

setup(
    name='pocket-lint-jshint',
    version='0.1.0',
    maintainer="Adi Roiban",
    maintainer_email="adi.roiban@chevah.com",
    url="https://github.com/chevah/pocket-lint-jshint",
    license='BSD license',
    description='JSHint suppor for pocket-lint.',
    long_description=open('README.rst').read(),
    packages=['pocketlint', 'pocketlint.jshint'],
    package_dir={'pocketlint.jshint': 'jshint'},
    package_data={'': ['README.rst', '*.js']}
)
