#!/usr/bin/env python
"""
    KVM automation for automating virtual machines using Bash and Python.
    Copyright (C) 2018 Mitch O'Donnell devreap1@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import argparse

class VirtInstall(object):
    """Parse arguments for virt-install."""
    def __init__(self, arg):
        pass
        

def create_snapshot_arguments():
    """Accept arguments to take a snapshot.
        virsh snapshot-create-as --domain <name from virsh list> \
        --name <new snapshot name>
    """
    description = '[*] KVM automation for automating virtual machines using Bash and Python.'
    github_url = 'https://github.com/BuildAndDestroy/automate_kvm'
    epilog = 'Github reference:\n[*] {}\n\r'.format(github_url)

    parser = argparse.ArgumentParser(description=description, epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)

    required_name = parser.add_argument_group('Required arguments for snapshot creation')

    required_name.add_argument('-d', '--domain', nargs=1, type=str, help='Provide hostname for snapshot.', required=True)
    required_name.add_argument('-n', '--name', nargs=1, type=str, help='provide name for new snapshot being created.', required=True)

    args = parser.parse_args()
    return args

def virt_install_arguments():
    """Arguments compiled to create KVM guest on a RedHat/CentOS host.
        Bash example:
        virt-install --name python-prep \
        --vcpu 2 \
        --ram 2048 \
        --location http://mirror.centos.org/centos/6/os/x86_64/ \
        --os-variant rhel6 \
        --disk /var/lib/libvirt/images/python-prep.qcow2,size=8 \
        --network bridge=virbr0 \
        --graphics none \
        --extra-args "console=ttyS0"
    """
    description = '[*] KVM automation for automating virtual machines using Bash and Python.'
    github_url = 'https://github.com/BuildAndDestroy/automate_kvm'
    epilog = 'Github reference:\n[*] {}\n\r'.format(github_url)

    parser = argparse.ArgumentParser(
        description=description, epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-i', '--initrd_inject', nargs='*', type=str,
                        help='Inject scripts, such as a kickstart, into the initramfs.')
    parser.add_argument('-e', '--extra_args', nargs='*', type=str,
                        help='Apply extra arguments to install.\nExample: console=ttyS0')
    parser.add_argument('-L', '--License', action='store_true',
                        help='Display shortened License.\nRead LICENSE file for full license.')

    required_name = parser.add_argument_group(
        'Required arguments for guest creation')

    required_name.add_argument('-n', '--name', nargs=1, type=str,
                               help='Provide a hostname for the guest.', required=True)
    required_name.add_argument('-c', '--vcpus', nargs=1, type=int,
                               help='Number of CPU cores to be used on the KVM.', required=True)
    required_name.add_argument('-r', '--ram', nargs=1, type=int,
                               help='Number of Megabytes of memory to use, 1Gig=1024.',
                               required=True)
    required_name.add_argument('-l', '--location', nargs=1, type=str,
                               help='Location of installer.\nThis can be a mirror at HTTP or an iso.',
                               required=True)
    required_name.add_argument('-o', '--os_variant', nargs=1, type=str,
                               help='Operating System flavor.\nExample: rhel7', required=True)
    required_name.add_argument('-d', '--disk', nargs=2,
                               help='Provide a directory for your disk path and size of disk in GB.\nExample: -d /var/lib/libvirt/images/centos7.qcow2 size=60', required=True)
    required_name.add_argument('-b', '--bridge', nargs=1, type=str,
                               help='Host device name for connecting networking.\nExample: "virbr0"',
                               required=True)
    required_name.add_argument('-g', '--graphics', action='store_true',
                               help='Currently supports "none", install happens in terminal.',
                               required=True)

    args = parser.parse_args()
    args = vars(args)
    return args


def main():
    """Library that contains argparses for each script."""
    print '[*] Library that contains argparses for each script.'


if __name__ == '__main__':
    main()