#!/usr/bin/env python
"""
    To install:
    Change to the directory you have cloned this git repo and run:
    "sudo pip install ."
"""

from setuptools import setup

__version__ = '2.7-virt-json'
packages = ['virsh_installs', 'snapshots', 'lib']
commands = ['kvm_virsh_install = virsh_installs.virt_install:main',
            'kvm_virsh_snapshot = snapshots.virsh_snapshot:main']

setup(
    name                = 'automate_kvm',
    version             = __version__,
    description         = 'KVM automation tool for creating guests within a host.',
    author              = 'Mitch O\'Donnell',
    author_email        = 'devreap1@gmail.com',
    packages            = packages,
    url                 = 'https://github.com/BuildAndDestroy/automate_kvm',
    license             = open('LICENSE').read(),
    install_requires    = [],
    entry_points        = {'console_scripts': commands},
    prefix              = '/opt/automate_kvm',
    long_description    = open('README.md').read()
)
