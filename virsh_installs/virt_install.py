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


def main():
    """Run the kvm_installer script."""
    args = virt_install_arguments()
    print args

    # example subprocess that works:
    #subprocess.call(['virt-install', '--name', 'centos_python', '--vcpus', '2', '--ram', '2048', '--location', 'http://mirror.centos.org/centos/6/os/x86_64/', '--os-variant', 'rhel6', '--disk', 'size=8', '--network', 'bridge=virbr0', '--graphics', 'none', '--extra-args', '"console=ttyS0"'])

    if __name__ == '__main__':
        main()
