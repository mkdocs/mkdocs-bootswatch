title: Home

# MkDocs Bootstrap Theme

This project provides [MkDocs] themes for the different Bootstrap themes
provided by the [Bootswatch] project.


## Installation & Usage

Install the collection of themes with pip, which is hopefully how you
installed MkDocs.

    pip install mkdocs-bootswatch


After installation is complete, edit your [mkdocs.yml] config file and set the
[theme] to one of the following Bootwatch themes included. The full list is as
follows:

 - [cerulean](#cerulean)
 - [cosmo](#cosmo)
 - [cyborg](#cyborg)
 - [flatly](#flatly)
 - [journal](#journal)
 - [simplex](#simplex)
 - [slate](#slate)
 - [spacelab](#spacelab)
 - [united](#united)
 - [yeti](#yeti)

For example:

    theme: cerulean

Or:

    theme: yeti

As with the base `mkdocs` theme, you can request alternate colors for the
navigation header. Allowed values are `primary` (the default), `dark`, and
`light`:

    theme:
        name: cerulean
        nav_style: dark

## Screenshots

This [documentation] is rendered with the Bootswatch [Flatly](#flatly) theme.
Previews of the other themes can be seen below.

### Cerulean
![Cerulean](/screenshots/cerulean.png)

### Cosmo
![Cosmo](/screenshots/cosmo.png)

### Cyborg
![Cyborg](/screenshots/cyborg.png)

### Flatly
![Flatly](/screenshots/flatly.png)

### Journal
![Journal](/screenshots/journal.png)

### Simplex
![Simplex](/screenshots/simplex.png)

### Slate
![Slate](/screenshots/slate.png)

### Spacelab
![Spacelab](/screenshots/spacelab.png)

### United
![United](/screenshots/united.png)

### Yeti
![Yeti](/screenshots/yeti.png)

[Mkdocs]: http://www.mkdocs.org
[mkdocs.yml]: http://www.mkdocs.org/user-guide/configuration/
[theme]: http://www.mkdocs.org/user-guide/configuration/#theme
[documentation]: http://mkdocs.github.io/mkdocs-bootstrap/
[Bootswatch]: https://bootswatch.com/
