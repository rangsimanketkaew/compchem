# Archive

## Casper

**Prerequisites**

| Language | MPI wrapper |
|----------|-------------|
| C | mpicc |
| C++ | mpiCC, mpicxx, mpic++ |
| FORTRAN | mpifort, mpif77, mpif90 |

MPI wrapper must be in `$PATH` environment variable.

**Installation**

```
tar -xzvf casper*.tar.gz
cd casper*
./configure --prefix=/where/you/wanna/install/casper/
make FC=mpiifort CC=mpiicc
make install
ls /where/you/wanna/install/casper/
```
