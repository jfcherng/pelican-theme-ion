# Demo

https://jfcherng.github.io/Pelican-Test/


# Installation

You may install dependencies via one of the following commands:

- `$ python3 -m pip install -U -r requirements.txt`
- `$ python3 -m pip install -U pelican beautifulsoup4 webassets cssmin jsmin`


# Used Pelican Plugins

```python
PLUGINS = [
    'assets',
    'headerid', # must before "bootstrap-rst"
    'bootstrap-rst',
    'pelican-toc', # https://github.com/ingwinlu/pelican-toc
    'related_posts',
]
```


# Notes

- [reStructuredText Quick Start](http://docutils.sourceforge.net/docs/user/rst/quickref.html)
- [Use a specific static page as the homepage](http://docs.getpelican.com/en/stable/faq.html#how-can-i-use-a-static-page-as-my-home-page)


Supporters <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=ATXYY9Y78EQ3Y" target="_blank"><img src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" /></a>
==========

Thank you guys for sending me some cups of coffee.
