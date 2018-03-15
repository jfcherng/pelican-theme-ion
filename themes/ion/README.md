# Pelican-theme-ion


## Dependencies

- Python modules (Could be installed via `pip`):

    - beautifulsoup4
    - webassets
    - cssmin
    - jsmin

- [Pelican plugins](https://github.com/getpelican/pelican-plugins):

    ```python
    PLUGINS = [
        'assets',
        'headerid', # must before "bootstrap-rst"
        'bootstrap-rst',
        'pelican-toc', # https://github.com/ingwinlu/pelican-toc
        'related_posts',
    ]
    ```


## Acknowledgment

This Pelican theme is modified from the [ion](https://templated.co/ion) theme.
