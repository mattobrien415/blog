#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGIN_PATH = "pelican-plugins"

AUTHOR = u"Matt O'Brien"
SITENAME = u"Matt O'Brien (is) Me"
SITEURL = ''


PLUGINS = ["render_math"]

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Spencer Boucher', 'http://spencerboucher.com/'),
          ('Trevor Stephens', 'http://trevorstephens.com/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10


# Static paths will be copied without parsing their contents
STATIC_PATHS = ['images', 'extra']

# Shift the installed location of a file
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

TWITTER_USERNAME = 'digitizerSF'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
