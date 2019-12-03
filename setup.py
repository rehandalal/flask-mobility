"""
A Flask extension to simplify building mobile-friendly sites.

Full documentation is available at:
http://flask-mobility.readthedocs.org/en/latest/
"""
import os
import sys

from setuptools import find_packages, setup
from setuptools.command.install import install

ROOT = os.path.abspath(os.path.dirname(__file__))

version = __import__("flask_mobility").__version__


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""

    description = "verify that the git tag matches our version"

    def run(self):
        tag = os.getenv("CIRCLE_TAG")

        if tag != "v{}".format(version):
            info = "Git tag: {0} does not match the version of this app: {1}".format(tag, version)
            sys.exit(info)


setup(
    name="Flask-Mobility",
    version=version,
    url="https://github.com/rehandalal/flask-mobility",
    license="Mozilla Public License Version 2.0",
    author="Rehan Dalal",
    author_email="rehan@meet-rehan.com",
    description="A Flask extension to simplify building mobile-friendly sites.",
    long_description=__doc__,
    packages=find_packages(exclude=["tests", "docs"]),
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    install_requires=["Flask"],
    py_modules=["flask_mobility"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    cmdclass={"verify": VerifyVersionCommand},
)
