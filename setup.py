import os
from setuptools import setup, find_packages
 
import django_kit
 
LONG_DESCRIPTION = open('README.rst').read()
 
setup(
    name='django-kit',
    version=django_kit.__version__,
    description="A set of useful helpers for my needs. Like django-annoying",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='django',
    author=django_kit.__author__,
    author_email='sun.void@gmail.com',
    url='http://github.com/uruz/django-kit',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
)