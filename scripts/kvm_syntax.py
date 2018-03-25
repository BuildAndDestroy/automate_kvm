#!/usr/bin/env python
"""
    KVM automation for automating virtual machines using Bash and Python.
    Copyright (C) 2018  Mitch O'Donnell devreap1@gmail.com

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


def parse_arguments():
    """Arguments compiled to create KVM guest on a RedHat/CentOS host."""
    description = '[*] KVM automation for automating virtual machines using Bash and Python.'
    github_url = 'https://github.com/BuildAndDestroy/automate_kvm'
    epilog = 'Github reference:\n[*] {}\n\r'.format(github_url)

    parser = argparse.ArgumentParser(
        description=description, epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-i', '--initrd-inject', nargs=1, type=str,
                        help='Inject scripts, such as a kickstart, into the initramfs.')
    parser.add_argument('-e', '--extra-args', nargs='*', type=str,
                        help='Apply extra arguments to install.\nExample: console=ttyS0')
    parser.add_argument('-L', '--License', action='store_true',
                        help='Display shortened License.\nRead LICENSE file for full license.')

    required_name = parser.add_argument_group(
        'Required arguments for guest creation')

    required_name.add_argument('-n', '--name', nargs=1, type=str,
                               help='Provide a hostname for the guest.', required=True)
    required_name.add_argument('-c', '--vcpu', nargs=1, type=int,
                               help='Number of CPU cores to be used on the KVM.', required=True)
    required_name.add_argument('-r', '--ram', nargs=1, type=int,
                               help='Number of Megabytes of memory to use, 1Gig=1024.',
                               required=True)
    required_name.add_argument('-l', '--location', nargs=1, type=str,
                               help='Location of installer.\nThis can be a mirror at HTTP or an iso.',
                               required=True)
    required_name.add_argument('-o', '--os-variant', nargs=1, type=str,
                               help='Operating System flavor.\nExample: rhel7', required=True)
    required_name.add_argument('-d', '--disk-size', nargs=1, type=int,
                               help='Provide a number, this will be the disk size in Gigs.',
                               required=True)
    required_name.add_argument('-b', '--bridge', nargs=1, type=str,
                               help='Host device name for connecting networking.\nExample: "virbr0"',
                               required=True)
    required_name.add_argument('-g', '--graphics', action='store_true',
                               help='Currently supports "none", install happens in terminal.',
                               required=True)

    args = parser.parse_args()
    return args


def main():
    """Run the kvm_installer script."""
    args = parse_arguments()
    print args

    if __name__ == '__main__':
        main()
