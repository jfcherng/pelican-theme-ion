# Pelican Theme: ION

[![Travis (.org) branch](https://img.shields.io/travis/jfcherng/pelican-theme-ion/master?style=flat-square)](https://travis-ci.org/jfcherng/pelican-theme-ion)
[![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/jfcherng/pelican-theme-ion?style=flat-square&logo=github)](https://github.com/jfcherng/pelican-theme-ion/tags)
[![Project license](https://img.shields.io/github/license/jfcherng/pelican-theme-ion?style=flat-square&logo=github)](https://github.com/jfcherng/pelican-theme-ion/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/jfcherng/pelican-theme-ion?style=flat-square&logo=github)](https://github.com/jfcherng/pelican-theme-ion/stargazers)
[![Donate to this project using Paypal](https://img.shields.io/badge/paypal-donate-blue.svg?style=flat-square&logo=paypal)](https://www.paypal.me/jfcherng/5usd)

## Demo

https://ecsme.ee.nthu.edu.tw

## Installation

You can install dependencies via `python3 -m pip install -U -r requirements.txt`.

## Used Pelican Plugins

```python
PLUGINS = [
    "assets",
    "headerid", # must before "bootstrap-rst"
    "bootstrap-rst",
    "pelican-toc", # https://github.com/jfcherng/pelican-toc
    "related_posts",
]
```

## Notes

- [reStructuredText Quick Start](http://docutils.sourceforge.net/docs/user/rst/quickref.html)
- [Use a specific static page as the homepage](http://docs.getpelican.com/en/stable/faq.html#how-can-i-use-a-static-page-as-my-home-page)
