#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import time

# default using English language
from .languages.en_US import *

TOC = {
    # What headers should be included in the generated toc
    # Expected format is a regular expression
    "TOC_HEADERS": r"^[hH]\d+",
    # Default value for toc generation,
    # if it does not evaluate to 'true' no toc will be generated
    "TOC_RUN": "true",
    # If 'true' include title in toc
    "TOC_INCLUDE_TITLE": "false",
}

# -------------------------#
# pre-generated variables #
# -------------------------#

ION_COPYRIGHT_YEAR_BASE = 2018
ION_COPYRIGHT_YEAR = "-".join(map(str, sorted({ION_COPYRIGHT_YEAR_BASE, int(time.strftime("%Y"))})))

# --------------------------------------#
# jfcherng-ion template configurations #
# --------------------------------------#

ION_ASSETS_MINIFY = False
ION_FONTS = []
ION_GOOGLE_ANALYTICS = ""
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
ION_DATE_FORMAT = "%Y/%m/%d"
ION_SHOW_AUTHORS_ON_ARTICLE = True
ION_SHOW_PUBLISHED_DATE_ON_ARTICLE = True
ION_SHOW_MODIFIED_DATE_ON_ARTICLE = True
ION_SHOW_CATEGORY_ON_ARTICLE = True
ION_SHOW_TAGS_ON_ARTICLE = True
ION_SHOW_TOC_ON_ARTICLE = False
ION_SHOW_AUTHORS_ON_PAGE = False
ION_SHOW_PUBLISHED_DATE_ON_PAGE = True
ION_SHOW_MODIFIED_DATE_ON_PAGE = True
ION_SHOW_TAGS_ON_PAGE = True
ION_SHOW_TOC_ON_PAGE = False

ION_BACKGROUND_PARTICLE = False
ION_SCROLL_UP_WIDGET = True
ION_HEADER_TITLE = ""
ION_BANNER_IMAGE = "theme/images/banner.jpg"
ION_BANNER_TITLE = "This is the banner title."
ION_BANNER_TITLE_EXTRA = "This is the banner extra title."
ION_BANNER_SUBTITLE = "This is the banner subtitle."
ION_FOOTER_IMAGE = ""
ION_FOOTER_EXTRA_CLASS = ""  # assign "light" to use a white footer
ION_FOOTER_HTML = ""  # HTML before fotter copyright
ION_COPYRIGHT = "Copyright &copy; {} {}".format(
    ION_COPYRIGHT_YEAR, '<a href="https://github.com/jfcherng">Jack Cherng</a>'
)
ION_EXTRA_HEAD_HTML = ""
ION_EXTRA_BOTTOM_HTML = ""
