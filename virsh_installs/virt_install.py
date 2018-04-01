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


from lib.arguments import virt_install_arguments
from lib.subprocesses import call_subprocess


def format_virt_install(args):
    """Pull the keys to format the values, then build the virt-install command."""
    virt_install_command = ['virt-install']
    args.pop('License')

    if args['initrd_inject'] is None:
        del args['initrd_inject']
    else:
        args['initrd_inject'] = args['initrd_inject'][0]

    if args['extra_args'] is None:
        del args['extra_args']
    else:
        args['extra-args'] = args.pop('extra_args')
        args['extra-args'] = ' '.join(args['extra-args'])

    args['name'] = args['name'][0]
    args['ram'] = args['ram'][0]
    args['vcpus'] = args['vcpus'][0]
    args['disk'] = 'path=' + ','.join(args['disk'])
    args['graphics'] = 'none'
    args['location'] = args['location'][0]
    
    args['os-variant'] = args.pop('os_variant')
    args['os-variant'] = args['os-variant'][0]

    args['network'] = args.pop('bridge')
    args['network'] = 'bridge:' + ''.join(args['network'])

    for key, value in args.iteritems():
        virt_install_command.append('--{} {}'.format(key, value))
    return virt_install_command


def main():
    """Run the kvm_installer script."""
    args = virt_install_arguments()
    #print args

    virt_install = format_virt_install(args)
    print virt_install

    call_subprocess(virt_install)

    # example subprocess that works:
    #subprocess.call(['virt-install', '--name', 'centos_python', '--vcpus', '2', '--ram', '2048', '--location', 'http://mirror.centos.org/centos/6/os/x86_64/', '--os-variant', 'rhel6', '--disk', 'size=8', '--network', 'bridge=virbr0', '--graphics', 'none', '--extra-args', '"console=ttyS0"'])

    if __name__ == '__main__':
        main()
