from setuptools import setup, find_packages
from distutils.core import Command
import os

VERSION = '0.4.0'


class generate_themes(Command):
    """ Generate complete themes from respective parts. """

    description = 'generate complete themes from respective parts'

    user_options = [
        ('force', 'f', 'forcibly build everything (ignore file timestamps)')
    ]

    boolean_options = ['force']

    def initialize_options(self):
        self.force = None

    def finalize_options(self):
        self.set_undefined_options(
            'build',
            ('force', 'force')
        )

    def run(self):
        """ Copy respective parts of themes to destination. """
        base = os.path.join('src', '_base')
        for theme in os.listdir('src'):
            srcdir = os.path.join('src', theme)
            if os.path.isdir(srcdir) and srcdir != base:
                outdir = os.path.join('mkdocs_bootswatch', theme)
                self.copy_tree(base, outdir)
                self.copy_tree(srcdir, outdir)


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
    cmdclass={
        'gen_themes': generate_themes,
    },
    entry_points={
        'mkdocs.themes': [
            'amelia = mkdocs_bootswatch.amelia',
            'cerulean = mkdocs_bootswatch.cerulean',
            'cosmo = mkdocs_bootswatch.cosmo',
            'cyborg = mkdocs_bootswatch.cyborg',
            'flatly = mkdocs_bootswatch.flatly',
            'journal = mkdocs_bootswatch.journal',
            'readable = mkdocs_bootswatch.readable',
            'simplex = mkdocs_bootswatch.simplex',
            'slate = mkdocs_bootswatch.slate',
            'spacelab = mkdocs_bootswatch.spacelab',
            'united = mkdocs_bootswatch.united',
            'yeti = mkdocs_bootswatch.yeti',
        ]
    },
    zip_safe=False
)
