# Note on install quantum chemistry packages

## NWChem
### Install NWChem on CentOS without root

- Download dependencies packages (rpm files) from https://centos.pkgs.org/ or https://rpmfind.net/
```
global array...
openblas...
scalapack..
openmpi...
```

- Download `nwchem-common` and `nwchem` rpm files from https://centos.pkgs.org/
```
$ ls
nwchem-common-7.0.0-6.el7.noarch.rpm
nwchem-openmpi-7.0.0-6.el7.x86_64.rpm
```

- Install packages using `rpm2cpio` command
```
rpm2cpio nwchem-common-7.0.0-6.el7.noarch.rpm | cpio -idv
rpm2cpio nwchem-openmpi-7.0.0-6.el7.x86_64.rpm | cpio -idv
```

NWChem will be installed in your `$HOME/usr/` directory at `$HOME/usr/lib64/openmpi/bin/nwchem_openmpi`.
