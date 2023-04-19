Changelog
=========


.. You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst

.. towncrier release notes start

2.0.1 (2023-04-19)
------------------

Internal:


- Update configuration files.
  [plone devs] (3333c742)


2.0.0 (2023-03-14)
------------------

Breaking changes:


- Drop compatibility with Plone 5.2 and lower.
  [maurits] (#60)


1.2.1 (2021-08-10)
------------------

Bug fixes:


- Return False when a url is not like a string, for example None.
  Note: this is not a security fix.
  [maurits] (#8)


1.2.0 (2021-07-31)
------------------

New features:


- Treat urls like ``https:example.org`` without slashes as outside the portal.
  Some browsers would redirect to example.org, some would redirect to a non-existing local page.
  We never want this, because this is likely a hack attempt.
  This vulnerability was discovered and reported by Yuji Tounai of Mitsui Bussan Secure Directions, Inc.
  See `security advisory 1 <https://github.com/plone/Products.isurlinportal/security/advisories/GHSA-q3m9-9fj2-mfwr>`_.
  [maurits] (#1)


1.1.1 (2020-09-07)
------------------

Bug fixes:


- Add testing for Python 3.6 + 3.8; add Python 3.8 trove classifier.
  [tschorr] (#3)


1.1.0 (2020-08-16)
------------------

New features:


- Harden against tricky whitespace in urls.
  [maurits] (#1)


1.0.0 (2020-07-21)
------------------

- Initial release.
  Code is the same as current Plone 4.3.19, 5.1.6, 5.2.1, with the January 2020 hotfix applied, plus compatibility fixes.
  [maurits]
