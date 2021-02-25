#!/usr/bin/env python3

# --------------------------------------------
# Convert CIF to XYZ
# Rangsiman Ketkaew
# Usage: $ cif2xyz.py input.cif
# --------------------------------------------


import sys
import os
import re
import pandas as pd
import numpy as np
import pymatgen as pmg
import warnings
warnings.filterwarnings('ignore')


def cif_to_xyz(cif, out):
    """Convert structure from CIF format to XYZ (Cartesian coordinate) format.
    """
    structure = pmg.Structure.from_file(cif)
    num_atoms = structure.num_sites
    dat = structure.as_dataframe()
    dat = dat.rename(columns={'Species': 'elements'})
    dat = dat[['elements', 'x', 'y', 'z']]
    dat['elements'] = dat['elements'].apply(lambda x: re.sub('\d+', '', str(x)))
    dat = dat.round(8)

    with open(str(out)+'.xyz', 'w') as f:
        f.write(str(num_atoms)+'\n'+'\n')
        f.write(dat.to_string(header=None, index=None, col_space=0))
        f.close()
    print(f"XYZ coordinates file has been saved: {out}.xyz")

    return dat


if __name__ == '__main__':
    try:
        cif = sys.argv[1]
    except IndexError:
        exit("Please specify CIF structure")
    filename = os.path.splitext(cif)[0]
    cif_to_xyz(cif, filename)

