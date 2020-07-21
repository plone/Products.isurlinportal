isURLInPortal patch for Plone
=============================

This patches the ``isURLInPortal`` method in Plone.
The method is in ``Products.CMFPlone/URLTool.py`` in the ``URLTool`` class.
Basic use in a page template is::

  <a
    tal:define="url request/came_from"
    tal:attributes="href url"
    tal:condition="python:context.portal_url.isURLInPortal(url)">
      This link is only shown when it is somewhere in the Plone portal.
  </a>


What does isURLInPortal do?
---------------------------

The ``isURLInPortal`` method in Plone is used in several places.
It checks if a url is (probably) within the current Plone Site.
If so, then this url is safe to redirect to, or is safe to show on a page.

For example, if your site is ``http://demo.plone.org``, then these urls are in the site:

- Full url: ``http://demo.plone.org/some-folder/some-page``
- Relative url: ``some-folder/some-page``, ``/somewhere/else``, ``../in/parent``

And these are not in the site:

- ``example.org``
- ``otherdomain.plone.org``

The code does *not* check if something is actually found at the url.
It only checks if the url would be within the site.

If this method fails to do its job, then an attacker could do a successful hack.
An attack can look like this:

- An attacker sends you an email with a specially crafted link.
  Or the attacker posts this link on a popular site that you visit.
- The link is to a Plone Site that you know and trust, so you click it.
- You see the expected Plone Site.  Maybe you login, but this may not be needed.

And then one of the following things happens:

- Open redirection: Somewhere on the page is a link to a malicious site.
  In a fishing attack, this site may look like the Plone Site you expect.
- Open redirection: You are *automatically* redirected to a malicious site.
- Reflected XSS (Cross Site Scripting):
  Malicious javascript is loaded that grabs private information from the page and sends it to the attacker.
  Or it is used to create content in your name, with more malicious code, or with spam.
- Stored XSS: If you are logged in as Editor in Plone, malicious javascript is stored, which is loaded by other visitors.

Let's not list the sort of urls that might have tricked this method in the past:
there is no need to give hackers and script kiddies more ideas.


Hotfixes
--------

During the years, there have been various security hotfixes that patch this method.
Usually this is because someone has alerted the `Plone Security Team <mailto:security@plone.org>`_ to a possible hack.
If we see that there is indeed a security problem, then we have to decide whether to publish a hotfix or not.

It may feel like overkill to create a hotfix for this and alert the entire Plone community, advising them to patch all their sites.
A lot of them may not be vulnerable.
For example:

- Modern browsers have protection against some of this, especially reflected XSS.
  We have had reports that we could not initially reproduce because of this.
- Some attacks are only for authenticated users.
  The frontend web server may have been setup to redirect the login form to a server that is only available internally.
- Some attacks are only for sites that have open registration, where everyone can make an account.
  This is probably not the case for most Plone sites.
- There may be a firewall in place that protects against these attacks.
  The vulnerable request may not even reach Plone.

An extra problem: multiple hotfixes patch the same method.
If you have Plone 4.3.0, and you have installed all hotfixes, then you have eleven of them.
Several of these patch this method.
If you load the oldest hotfix first, then it should work okay.
The other way around may even also work, although it is not recommended.

But we don't test the hotfixes in combination with *all* other hotfixes.
We sometimes test with a few though, and in some cases a new hotfix explicitly tries to load an older hotfix first.

And it has a (probably small) impact on performance:
most hotfixed versions of this method do their specific check, and then call the original method.
So it may look like this:

- A call is made to ``isURLInPortal``.
- This method is patched by ``PloneHotfix20200121``, so it executes its own code, and then calls the original method.
- This method is patched by ``PloneHotfix20171128``, so it executes its own code, and then calls the original method.
- This finally is the code in ``CMFPlone``.
- The three versions have overlap, leading to the same code being executed two or three times.


Idea: separate package
----------------------

The idea now is: let's put this method into a separate package.
This package would work as hotfix for all current Plone versions, or at least 4.3 and higher.
Newer releases of CMFPlone would depend on this package, so it is automatically included.
The new package would be the canonical place of the method.
We would remove the method from newer CMFPlone releases.

If a new vulnerability is then detected, we would fix it and release a new version of this package.
Fixing your site would then be:

- Edit the version number of the new package in the versions section of your buildout.
- Stop the site.
- Run buildout.
- Start the site.

We could still announce it as a hotfix if we want.

Since all hotfixes are in the ``Products`` namespace, we put this package in the same namespace.
Code in this namespace is automatically loaded by Plone/Zope.
Also, this makes it easier to extract the main directory (``isurlinportal``) of this package and put it in an old-style ``products`` folder.
Then you can just restart Plone without having to run buildout.
This is mainly an issue for older Plone sites that have not been maintained well.


Version numbers
---------------

You should always use the latest version of this package that is compatible with your Plone version.

- Major/breaking release, X.0.0:
  Likely a new vulnerability was patched.
  Please update as soon as possible.
  But this may drop support for an older Plone or Python version, so read the changelog.
  If you have an older Plone, check if there is an older update.
- Minor/feature release: x.Y.0:
  A new vulnerability was patched.
  Please update as soon as possible.
- Micro/bugfix release: x.y.Z:
  A bug was fixed, but no new vulnerability was patched.
  Update at a time of your choosing, or if you experience problems.


Reporting vulnerabilities or bugs
---------------------------------

If you suspect you have found a vulnerability, please contact the `Plone Security Team <mailto:security@plone.org>`_ by email.
If you prefer a more secure way, we can also arrange that via email.

If you see a non-security bug, you can open an issue, or create a pull request.
When in doubt, please email us.
