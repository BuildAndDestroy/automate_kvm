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

import json

from lib.arguments import virt_install_arguments
from lib.subprocesses import call_subprocess


def format_virt_install(args):
    """Pull the keys to format the values, then build the virt-install command."""
    virt_install_command = ['virt-install']
    special_arguments = []
    single_argument = []
    args.pop('License')

    if args['initrd_inject'] is None:
        del args['initrd_inject']
    else:
        args['initrd-inject'] = args.pop('initrd_inject')
        args['initrd-inject'] = ' '.join(args['initrd-inject'])

    if args['extra_args'] is None:
        del args['extra_args']
    else:
        args['extra-args'] = args.pop('extra_args')
        args['extra-args'] = ' '.join(args['extra-args'])

    args['nographics'] = args.pop('graphics')

    args['name'] = args['name'][0]
    args['ram'] = args['ram'][0]
    args['vcpus'] = args['vcpus'][0]
    args['disk'] = 'path=' + ','.join(args['disk'])
    args['location'] = args['location'][0]

    args['os-variant'] = args.pop('os_variant')
    args['os-variant'] = args['os-variant'][0]

    args['network'] = args.pop('bridge')
    args['network'] = 'bridge:' + ''.join(args['network'])

    for key, value in args.iteritems():
        if key is 'extra-args':
            special_arguments.append('--{}'.format(key))
            special_arguments.append('{}'.format(value))
        elif key is 'initrd-inject':
            special_arguments.append('--{}={}'.format(key, value))
        elif key is 'nographics':
            single_argument.append('--{}'.format(key))
        else:
            virt_install_command.append('--{} {}'.format(key, value))
    return [virt_install_command, special_arguments, single_argument]

def format_json_quotes(virt_install):
    """
        Virt-install relies on extra args to be double quotes.
        Example:
        ["--initrd-inject=/root/kickstart/ks.cfg",
            "--extra-args", 
            "console=ttyS0 ks=file:/ks.cfg"]
    """
    return json.dumps(virt_install[1])


def format_for_subprocess(virt_install):
    """Format standard and spcial commands into split strings for subprocess to comprehend."""
    virsh_install = []
    virsh_commands_standard = virt_install[0]
    virsh_commands_special = virt_install[1]
    virsh_commands_single = virt_install[2]
    split_virsh_standard = [line.split() for line in virsh_commands_standard]

    for index in split_virsh_standard:
        for strings in index:
            virsh_install.append(strings)
    for index in virsh_commands_single:
        virsh_install.append(index)
    for index in virsh_commands_special:
        virsh_install.append(index)
    #print json.dumps(virsh_install)
    return virsh_install


def main():
    """Run the kvm_installer script."""
    args = virt_install_arguments()
    # print args # DEBUG

    virt_install = format_virt_install(args)
    # print virt_install # DEBUG
    extra_args = format_json_quotes(virt_install)
    send_to_subprocess = format_for_subprocess(virt_install)
    #print send_to_subprocess  # DEBUG
    call_subprocess(send_to_subprocess)

    if __name__ == '__main__':
        main()
