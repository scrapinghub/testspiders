from setuptools import setup, find_packages

setup(
    name         = 'testspiders',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = testspiders.settings']},
    scripts = ['bin/testargs.py']
)
