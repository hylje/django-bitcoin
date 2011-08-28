<<<<<<< HEAD
from distutils.core import setup

setup(name='django-bitcoin',
      version='1.0',
      description='bitcoin payment management for django',
      author='Jeremias Kangas',
      url='https://github.com/kangasbros/django-bitcoin',
      packages=['django_bitcoin', 
                'django_bitcoin.management',
                'django_bitcoin.management.commands',
                'django_bitcoin.jsonrpc'],
     )
=======
#!/usr/bin/env python

from setuptools import setup, find_packages

tests_require = [
    'django',
    # also requires the disqus fork of haystack
]

setup(
    name='django-ratings',
    version=".".join(map(str, __import__('djangoratings').__version__)),
    author='David Cramer',
    author_email='dcramer@gmail.com',
    description='Generic Ratings in Django',
    url='http://github.com/dcramer/django-ratings',
    install_requires=[
        'django',
    ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
    test_suite='djangoratings.runtests.runtests',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
>>>>>>> d0ae149d112c7e5f9f40bb04028ceac4bf4b0e0d
