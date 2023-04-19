from setuptools import find_packages
from setuptools import setup


with open("README.rst") as myfile:
    readme = myfile.read()
with open("CHANGES.rst") as myfile:
    changes = myfile.read()
long_description = readme + "\n" + changes


setup(
    name="Products.isurlinportal",
    version="2.0.1",
    description="Replacement for isURLInPortal method in Plone",
    long_description=long_description,
    # Get more strings from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="plone security hotfix patch",
    author="Plone Security Team",
    author_email="security@plone.org",
    url="https://github.org/plone/Products.isurlinportal",
    license="GPL",
    packages=find_packages(),
    namespace_packages=["Products"],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "setuptools",
        "plone.base",
    ],
    extras_require={
        "test": [
            "Products.CMFPlone",
        ]
    },
)
