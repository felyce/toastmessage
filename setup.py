#!/usr/bin/env python

from setuptools import setup

setup(name='django-toast-messages',
    version='0.0.1',
    description='jQuery-powered sexy floating messages',
    author='Arpaso',
    author_email='millioner.bbb@gmail.com',
    url='',
    packages=['toastmessage', ],
    include_package_data = True,    # include everything in source control
    zip_safe=False,
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Development Status :: 4 - Beta",
        'Environment :: Web Environment',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: User Interfaces",
        "Framework :: Django",
        ],
    long_description = """\
Django wrapper for using jQuery-powered sexy floating messages - http://akquinet.github.com/jquery-toastmessage-plugin/
"""
)
