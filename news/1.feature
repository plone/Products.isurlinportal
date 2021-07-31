Treat urls like ``https:example.org`` without slashes as outside the portal.
Some browsers would redirect to example.org, some would redirect to a non-existing local page.
We never want this, because this is likely a hack attempt.
This vulnerability was discovered and reported by Yuji Tounai of Mitsui Bussan Secure Directions, Inc.
See `security advisory 1 <https://github.com/plone/Products.isurlinportal/security/advisories/GHSA-q3m9-9fj2-mfwr>`_.
[maurits]
