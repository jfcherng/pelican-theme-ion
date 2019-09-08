# Pelican Theme: ION

<a href="https://travis-ci.org/jfcherng/pelican-theme-ion"><img alt="Travis (.org) branch" src="https://img.shields.io/travis/jfcherng/pelican-theme-ion/master?style=flat-square"></a>
<a href="https://github.com/jfcherng/pelican-theme-ion/tags"><img alt="GitHub tag (latest SemVer)" src="https://img.shields.io/github/tag/jfcherng/pelican-theme-ion?style=flat-square&logo=github"></a>
<a href="https://github.com/jfcherng/pelican-theme-ion/blob/master/LICENSE"><img alt="Project license" src="https://img.shields.io/github/license/jfcherng/pelican-theme-ion?style=flat-square&logo=github"></a>
<a href="https://github.com/jfcherng/pelican-theme-ion/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/jfcherng/pelican-theme-ion?style=flat-square&logo=github"></a>
<a href="https://www.paypal.me/jfcherng/5usd" title="Donate to this project using Paypal"><img src="https://img.shields.io/badge/paypal-donate-blue.svg?style=flat-square&logo=paypal"></a>


## Demo

https://ecsme.ee.nthu.edu.tw


## Installation

You can install dependencies via `$ python3 -m pip install -U -r requirements.txt`.


## Used Pelican Plugins

```python
PLUGINS = [
    "assets",
    "headerid", # must before "bootstrap-rst"
    "bootstrap-rst",
    "pelican-toc", # modified from https://github.com/ingwinlu/pelican-toc
    "related_posts",
]
```


## Notes

- [reStructuredText Quick Start](http://docutils.sourceforge.net/docs/user/rst/quickref.html)
- [Use a specific static page as the homepage](http://docs.getpelican.com/en/stable/faq.html#how-can-i-use-a-static-page-as-my-home-page)
