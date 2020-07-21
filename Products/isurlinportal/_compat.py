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

try:
    # Plone 5.0+
    from plone.registry.interfaces import IRegistry
    from Products.CMFPlone.interfaces import ILoginSchema
    from zope.component import getUtility

    def get_external_sites(context=None):
        # context is not used here
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ILoginSchema, prefix="plone")
        return settings.allow_external_login_sites


except ImportError:
    # Plone 4.3
    from Products.CMFCore.utils import getToolByName

    def get_external_sites(context=None):
        props = getToolByName(context, "portal_properties").site_properties
        return props.getProperty("allow_external_login_sites", [])
