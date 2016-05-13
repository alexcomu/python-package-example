import os

from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.md')).read()
except IOError:
    README = ''

version = "0.0.1"

#os.system('pip install ADDITIONAL-REQ')

setup(name='alexcomu',
      version=version,
      description="Simple example of Python Package using a structured config file.",
      long_description=README,
      author='alexcomu',
      license='MIT',
      zip_safe=False,
      packages=['alexcomu', ],
      entry_points={
          'console_scripts': [
              'alexcomu = alexcomu.main:main'
          ]
      },
      install_requires=[
          "pymongo == 2.7.2",
          "configparser"
      ]
)


