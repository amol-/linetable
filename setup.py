from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, "README.rst")).read()
except IOError:
    README = ""

version = "0.0.2"

setup(
    name="linetable",
    version=version,
    description="library to manage Python Locations Table (co_linetable)",
    long_description=README,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.11',
    ],
    keywords="",
    author="Alessandro Molina",
    author_email="amol@turbogears.org",
    url="https://github.com/amol-/linetable",
    license="MIT",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points="""
      # -*- Entry points: -*-
      """,
)
