from pathlib import Path
from setuptools import find_packages
from setuptools import setup


setup(
    name="Products.isurlinportal",
    version="3.0.1",
    description="Implementation of isURLInPortal method in Plone",
    long_description=(
        f"{Path('README.rst').read_text()}\n{Path('CHANGES.rst').read_text()}\n"
    ),
    # Get more strings from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: 6.2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    keywords="plone security hotfix patch",
    author="Plone Security Team",
    author_email="security@plone.org",
    url="https://github.org/plone/Products.isurlinportal",
    license="GPL",
    packages=find_packages("src"),
    namespace_packages=["Products"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "setuptools",
        "plone.base",
        "Zope>=5.10",
    ],
    extras_require={
        "test": [
            "Products.CMFPlone",
        ]
    },
)
