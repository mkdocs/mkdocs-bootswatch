from setuptools import setup, find_packages
from distutils.core import Command
import os

VERSION = '1.1'


setup(
    name="mkdocs-bootswatch",
    version=VERSION,
    url='http://www.mkdocs.org',
    license='BSD',
    description='Bootswatch themes for MkDocs',
    author='Dougal Matthews',
    author_email='dougal@dougalmatthews.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['mkdocs>=1.1'],
    python_requires='>=3.5',
    entry_points={
        'mkdocs.themes': [
            'cerulean = mkdocs_bootswatch.cerulean',
            'cosmo = mkdocs_bootswatch.cosmo',
            'cyborg = mkdocs_bootswatch.cyborg',
            'darkly = mkdocs_bootswatch.darkly',
            'flatly = mkdocs_bootswatch.flatly',
            'journal = mkdocs_bootswatch.journal',
            'litera = mkdocs_bootswatch.litera',
            'lumen = mkdocs_bootswatch.lumen',
            'lux = mkdocs_bootswatch.lux',
            'materia = mkdocs_bootswatch.materia',
            'minty = mkdocs_bootswatch.minty',
            'pulse = mkdocs_bootswatch.pulse',
            'sandstone = mkdocs_bootswatch.sandstone',
            'simplex = mkdocs_bootswatch.simplex',
            'slate = mkdocs_bootswatch.slate',
            'solar = mkdocs_bootswatch.solar',
            'spacelab = mkdocs_bootswatch.spacelab',
            'superhero = mkdocs_bootswatch.superhero',
            'united = mkdocs_bootswatch.united',
            'yeti = mkdocs_bootswatch.yeti',
        ]
    },
    zip_safe=False
)
