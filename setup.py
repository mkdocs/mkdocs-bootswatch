from setuptools import setup, find_packages

VERSION = '0.4.0'


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
