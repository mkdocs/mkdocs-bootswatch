# MkDocs Bootswatch Themes

See the documentation for more details:

http://mkdocs.github.io/mkdocs-bootswatch/

[![PyPI Downloads][pypi-dl-image]][pypi-dl-link]
[![PyPI Version][pypi-v-image]][pypi-v-link]
[![Build Status][travis-image]][travis-link]

[pypi-dl-image]: https://img.shields.io/pypi/dm/mkdocs-bootswatch.svg
[pypi-dl-link]: https://pypi.python.org/pypi/mkdocs-bootswatch
[pypi-v-image]: https://img.shields.io/pypi/v/mkdocs-bootswatch.svg
[pypi-v-link]: https://pypi.python.org/pypi/mkdocs-bootswatch
[travis-image]: https://img.shields.io/travis/mkdocs/mkdocs-bootswatch/master.svg
[travis-link]: https://travis-ci.org/mkdocs/mkdocs-bootswatch

## Contributing

Any contributions should make changes to the files in the `src` directory. Files
in the `src/_base` directory are common to all themes and any files in the
`src/<theme name>` directory are specific to `<theme name>`.

After the `src` files are updated, run the command `python setup.py gen_themes`,
which will update the compiled themes in the `mkdocs_bootswatch` directory. When
preparing a patch (pull request), be sure to include the changes in both the
`src` directory and the `mkdocs_bootswatch` directory.
