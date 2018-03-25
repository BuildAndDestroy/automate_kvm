#!/usr/bin/env python
"""
    To install:
    Change to the directory you have cloned this git repo and run:
    "sudo pip install ."
"""

#import pkg_resources
from setuptools import setup

__version__ = '1.0'
packages = ['scripts']
commands = ['kvm_installer = scripts.kvm_syntax:main']

setup(
    name                = 'automate_kvm',
    version             = __version__,
    description         = 'KVM automation tool for creating guests within a host.',
    author              = 'Mitch O\'Donnell',
    author_email        = 'devreap1@gmail.com',
    packages            = packages,
    url                 = '',
    license             = open('LICENSE').read(),
    install_requires    = [],
    entry_points        = {'console_scripts': commands},
    prefix              = '/opt/automate_kvm',
    long_description    = open('README.md').read()
)
