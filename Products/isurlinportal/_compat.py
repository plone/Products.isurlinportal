# We do not want to depend on the 'six' package for compatibility,
# because not all Plone versions may have it.

# from six.moves.urllib import parse
try:
    # Python 3
    from urllib.parse import urlparse
    from urllib.parse import urljoin
except ImportError:
    # Python 2
    from urlparse import urlparse
    from urlparse import urljoin

try:
    # Python 2
    from HTMLParser import HTMLParser

    hp = HTMLParser()
    unescape = hp.unescape

except ImportError:
    # Python 3
    import html

    unescape = html.unescape
