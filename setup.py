from setuptools import setup, find_packages
import sys, os, io

# List all of your Python package dependencies in the
# requirements.txt file

def readfile(filename, split=False):
    with io.open(filename, encoding="utf-8") as stream:
        if split:
            return stream.read().split("\n")
        return stream.read()

readme = readfile("README.md", split=True)[3:]  # skip title
requires = readfile("requirements.txt", split=True)
license = readfile("LICENSE")

setup(name=u'mapclientplugins.pointwiserigidregistrationstep',
    version='1.0.0',
    description='',
    long_description='
'.join(readme) + license,
    classifiers=[
      "Development Status :: 4 - Beta",
      "License :: OSI Approved :: Apache Software License",
      "Programming Language :: Python",
    ],
    author=u'Ju Zhang',
    author_email='',
    url='https://github.com/mapclient-plugins/pointwiserigidregistrationstep',
    license='APACHE',
    packages=find_packages(exclude=['ez_setup',]),
    namespace_packages=['mapclientplugins'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    )
