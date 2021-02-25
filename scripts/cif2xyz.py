#!/usr/bin/env python3

#--------------------------------------------
# Original written by gomezperalta
# https://github.com/gomezperalta/CrystMaker
# ---
# Edited by Rangsiman Ketkaew
#--------------------------------------------


import sys
import os
import pandas as pd
import numpy as np
import pymatgen as mg
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
import itertools
import warnings
warnings.filterwarnings('ignore')

def UnitCell(cif, out):
    structure=mg.Structure.from_file(cif)
    sga=SpacegroupAnalyzer(structure)
    archivo=sga.get_conventional_standard_structure()
    text=str(archivo)
    
    sitios=int(text.split('\n')[4].split('(')[1].split(')')[0])
    
        
    abc=[float(item) for item in list(filter(None,text.split('\n')[2].split(':')[1].split(' ')))]
    angles=[float(item) for item in list(filter(None,text.split('\n')[3].split(':')[1].split(' ')))]
    lista=text.split('\n')[-sitios:]
    
    #for i in range(len(lista)):
    #    print(lista[i])
    newlist=[list(filter(None,line.split(' '))) for line in lista]

    newlist=np.asarray(newlist)
    #print(newlist)    
    motif=pd.DataFrame(newlist)[[1,2,3,4]]
    motif[2]=[float(i) for i in motif[2].values]
    motif[3]=[float(i) for i in motif[3].values]
    motif[4]=[float(i) for i in motif[4].values]
    
    motif.columns = np.arange(len(motif.columns))
    
    motif[4]=1*(motif[1].values == 0)+1*(motif[2].values == 0)+1*(motif[3].values == 0) 
    
    motif_three=motif[motif[4] == 3].iloc[:,0:4].reset_index(drop=True) 
    motif_two=motif[motif[4] == 2].iloc[:,0:4].reset_index(drop=True) 
    motif_one=motif[motif[4] == 1].iloc[:,0:4].reset_index(drop=True) 
    motif=motif.iloc[:,0:4].reset_index(drop=True)

    #abc=np.loadtxt('abc.csv')
    #angles=np.loadtxt('angulos.csv')

    volumen=abc[0]*abc[1]*abc[2]*np.sqrt(1-(np.cos(np.deg2rad(angles[0])))**2-(np.cos(np.deg2rad(angles[1])))**2-(np.cos(np.deg2rad(angles[2])))**2+2*np.cos(np.deg2rad(angles[0]))*np.cos(np.deg2rad(angles[1]))*np.cos(np.deg2rad(angles[2])))

    matrix=np.array([[abc[0],abc[1]*np.cos(np.deg2rad(angles[2])),abc[2]*np.cos(np.deg2rad(angles[1]))],
                      [0,abc[1]*np.sin(np.deg2rad(angles[2])),abc[2]*(np.cos(np.deg2rad(angles[0]))-np.cos(np.deg2rad(angles[1]))*np.cos(np.deg2rad(angles[2])))/np.sin(np.deg2rad(angles[2]))],
                      [0,0,volumen/(abc[0]*abc[1]*np.sin(np.deg2rad(angles[2])))]])

    if len(motif_one) != 0:
        
        positions_one=motif_one.replace(0,1).iloc[:,1:].values
        #positions_one=np.round(np.matmul(xyz_one,matrix),4)
        positions_one=pd.DataFrame(positions_one)
        positions_one=positions_one.rename(columns={0:1,1:2,2:3})
        positions_one[0]=motif_one[0]
        motif=motif.append(positions_one, ignore_index=True)
        
    tras0=np.array(list(itertools.product([0,1],repeat=3)))[1:7]
    tras1=np.array(list(itertools.product([0,1],repeat=3)))[1:]
        
    if len(motif_two) != 0:
        for vector in tras0:
            
            positions_two=np.add(motif_two.iloc[:,1:].values,vector)
            data=pd.DataFrame(positions_two)
            data=data.rename(columns={0:1,1:2,2:3})
            data[0]=motif_two[0]
            data=data[[0,1,2,3]]
            data=data[data <= 1].dropna()
            data=data.reset_index(drop=True)
            motif=motif.append(data, ignore_index=True)

    if len(motif_three) != 0:
        for vector in tras1:
            
            positions_three=np.add(motif_three.iloc[:,1:].values,vector)
            positions_three=pd.DataFrame(positions_three)
            data=pd.DataFrame(positions_three)
            data=data.rename(columns={0:1,1:2,2:3})
            data[0]=motif_three[0]
            data=data[[0,1,2,3]]
            data=data[data <= 1].dropna()
            data=data.reset_index(drop=True)
            motif=motif.append(data, ignore_index=True)
    
    positions=np.round(np.matmul(motif.iloc[:,1:].values,matrix),4)
    positions=pd.DataFrame(positions)
    positions=positions.rename(columns={0:'x',1:'y',2:'z'})
    positions['element']=motif[0]
    
    positions['element']=positions['element'].map(lambda x: x.lstrip('+-').rstrip('0123456789:.'))
    positions['element']=positions['element'].map(lambda x: x.lstrip('0123456789.:').rstrip('+-:.'))
    positions['element']=positions['element'].str.replace('\d+','')
    
    
    positions=positions[['element','x','y','z']]
    positions=positions.round(4)
    atoms=len(positions)
    
    #positions.to_csv(str(out)+'.csv', header=None, index=None, sep='\t')
    
    with open(str(out)+'.xyz', 'w') as file:
        file.write(str(atoms)+'\n'+'\n')
        file.write(positions.to_string(header=None, index=None, col_space=0))
        file.close()
    print(f"XYZ coordinates file has been saved: {out}.xyz")
    
    return positions

if __name__ == '__main__':
    cif = sys.argv[1]
    filename = os.path.splitext(cif)[0]
    UnitCell(cif, filename)

