#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGIN_PATHS = ["pelican-plugins"]

THEME = 'Flex'


AUTHOR = u"Matt O'Brien"
SITENAME = u"Matt O'Brien (dot) Me"
SITEURL = 'http://www.mattobrien.me'

DISQUS_SITENAME = "mattobrienme"

PLUGINS = ["render_math"]

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

GOOGLE_ANALYTICS = 'UA-51519407-1'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Spencer Boucher', 'http://spencerboucher.com/'),
          ('Trevor Stephens', 'http://trevorstephens.com/'),)

# Social widget

TWITTER_USERNAME = 'digitizerSF'
TWITTER_WIDGET_ID = '472464593332097024'

SOCIAL = (('GitHub', 'https://github.com/mobbSF'),
          ('LinkedIn', 'http://www.linkedin.com/pub/matt-o-brien/5/833/91b/'),
          ('RSS', SITEURL + 'feeds/all.atom.xml'))
DEFAULT_PAGINATION = 10


# Static paths will be copied without parsing their contents
STATIC_PATHS = ['images', 'extra']

# Shift the installed location of a file
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}


MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.tables':{},
    }
}
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
