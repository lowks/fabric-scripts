#from distutils.core import setup
from setuptools import setup, find_packages

# http://guide.python-distribute.org/quickstart.html
# python setup.py sdist
# python setup.py register
# python setup.py sdist upload
# pip install fabric-scripts
# pip install fabric-scripts --upgrade --no-deps
# Manual upload to PypI
# http://pypi.python.org/pypi/fabric-scripts
# Go to 'edit' link
# Update version and save
# Go to 'files' link and upload the file

VERSION = '0.0.9'

tests_require = [
    'nose',
    'coverage',
    'nose',
    'tox',
    'flake8',
]

install_requires = [
    'fabric',
]

# from pip.req import parse_requirements
# install_requires = parse_requirements('requirements.txt')
# tests_require = parse_requirements('requirements-dev.txt')

setup(name='fabric-scripts',
      url='https://github.com/paulocheque/fabric-scripts',
      author="paulocheque",
      author_email='paulocheque@gmail.com',
      keywords='python django testing fixture',
      description='fabric-scripts',
      license='MIT',
      classifiers=[
          'Framework :: Django',
          'Operating System :: OS Independent',
          'Topic :: Software Development',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: Implementation :: PyPy',
      ],

      version=VERSION,
      install_requires=install_requires,
      tests_require=tests_require,
      test_suite='runtests.runtests',
      extras_require={'test': tests_require},

      entry_points={ 'nose.plugins': [] },
      packages=find_packages(),
)

