# Now Working

virt-install is now working manually and with kickstart files, see examples below:

# EXAMPLE

\#  kvm_virsh_install -n \<hostname> 
-c \<# of VCPUs> \\
-r \<# of ram in MB> 
-l \<location of mirror for install> 
-o \<Operating System name like "rhel7"> 
-d \<# of Gigs for volume size> 
-b \<Network bridge adapter> 
-g 
-i \<directory and file name for kickstart> 
-e \<additional arguments like output to terminal and the kickstart file name>

\#  kvm_virsh_install -n server-hostname 
-c 4
-r 4096 
-l http://centos.mirror.org/centos/7/os/x86_64/
-o rhel7.3
-d /var/lib/libvirt/images/centos7.qcow2 size=10 
-b virbr0
-g 
-i /root/anaconda.cfg
-e ks=file:/anaconda.cfg

# INSTALL

\# pip install automate_kvm/.


# UPGRADE

\# pip install --upgrade automate_kvm/.


# BUGS

Please open an issue on github and give terminal output. Please give details on how how to reproduce the issue as well.

