# MkDocs Bootswatch Themes

See the documentation for more details:

https://mkdocs.github.io/mkdocs-bootswatch/

[![PyPI Version][pypi-v-image]][pypi-v-link]
[![Build Status][travis-image]][travis-link]

[pypi-v-image]: https://img.shields.io/pypi/v/mkdocs-bootswatch.svg
[pypi-v-link]: https://pypi.python.org/pypi/mkdocs-bootswatch
[travis-image]: https://img.shields.io/travis/mkdocs/mkdocs-bootswatch/master.svg
[travis-link]: https://travis-ci.org/mkdocs/mkdocs-bootswatch

## Contributing

These themes all inherit from the `mkdocs` theme which ships with MkDocs. These
themes primarily contain CSS which replaces/overrides the CSS in the `mkdocs`
theme.  All other improvements should be made to the `mkdocs` theme in the
project hosted at <https://github.com/mkdocs/mkdocs>.

## Release Notes

### Version 1.1 (2020/02/22)

* Update to support MkDocs version 1.1.
* Update to support Bootstrap 4.
    * Remove the `amelia` and `readable` themes, which were dropped by Bootswatch.
    * Add Bootswatch's new themes: `darkly`, `litera`, `lumen`, `lux`, `materia`,
      `minty`, `pulse`, `sandstone`, `solar`, and `superhero`.
* Port changes from the parent `mkdocs` theme:
    * [Properly handle the scroll offset for anchors](https://github.com/mkdocs/mkdocs/pull/1935).
    * [Improve support for long dropdowns](https://github.com/mkdocs/mkdocs/pull/1967).
    * [Improve support for tall nav headers](https://github.com/mkdocs/mkdocs/pull/1969)
    * [Use toc_tokens to generate the TOC](https://github.com/mkdocs/mkdocs/pull/1970)
* Fix padding/background color issues with hljs code blocks.

### Version 1.0 (2018/08/03)

* Inherit from the `mkdocs` theme and get all the parent theme's features.
* Update to support MkDocs version 1.0.

### Version 0.5 (2018/02/16)

* Fix padding of code blocks
* Generate all themes from one common base.
* Update templates for MkDocs v0.17.
* Update per-theme CSS to match MkDocs.
* Update to FontAwesome 4.5.0.
* Improve code highlighting colors for all themes.
* Support admonitions.

### Version 0.4 (2016/03/02)

* Some styling tweaks.
* Add support for permalinks.
* Support inverse nav headers.

### Version 0.3.1 (2016/02/24)

* Fix docs deployment.

### Version 0.3 (2016/02/24)

* Add support for sub-level nav.

### Version 0.2 (2018/02/06)

* Add search modal to all themes.
* Automate releases.

### Version 0.1 (2015/06/23)

* Initial release.
