from setuptools import setup, find_packages
import io


def readfile(filename, split=False):
    with io.open(filename, encoding="utf-8") as stream:
        if split:
            return stream.read().split("\n")
        return stream.read()


package_readme = readfile("README.md", split=True)[3:]  # skip title
package_license = readfile("LICENSE")
package_dependencies = [
    "setuptools",
    "PySide2",
    "numpy",
    "gias2",
    "traits"
]

setup(name=u'mapclientplugins.pointwiserigidregistrationstep',
      version='1.0.1',
      description='',
      long_description='\n'.join(package_readme) + package_license,
      classifiers=[
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python",
      ],
      author=u'Ju Zhang',
      author_email='',
      url='https://github.com/mapclient-plugins/pointwiserigidregistrationstep',
      license='APACHE',
      packages=find_packages(exclude=['ez_setup', ]),
      namespace_packages=['mapclientplugins'],
      include_package_data=True,
      zip_safe=False,
      install_requires=package_dependencies,
      )
