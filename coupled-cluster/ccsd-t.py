#!/usr/bin/python

import math
import numpy as np

####################################
#
#   FUNCTIONS
#
####################################

# Return compound index given four indices


def eint(a, b, c, d):
    if a > b:
        ab = a*(a+1)/2 + b
    else:
        ab = b*(b+1)/2 + a
    if c > d:
        cd = c*(c+1)/2 + d
    else:
        cd = d*(d+1)/2 + c
    if ab > cd:
        abcd = ab*(ab+1)/2 + cd
    else:
        abcd = cd*(cd+1)/2 + ab
    return abcd

# Return Value of spatial MO two electron integral
# Example: (12\vert 34) = tei(1,2,3,4)


def teimo(a, b, c, d):
    return ttmo.get(eint(a, b, c, d), 0.0e0)

####################################
#
#  INITIALIZE ORBITAL ENERGIES
#  AND TRANSFORMED TWO ELECTRON
#  INTEGRALS
#
####################################


Nelec = 2  # we have 2 electrons in HeH+
dim = 2  # we have two spatial basis functions in STO-3G
E = [-1.52378656, -0.26763148]  # molecular orbital energies
# python dictionary containing two-electron repulsion integrals
ttmo = {5.0: 0.94542695583037617, 12.0: 0.17535895381500544, 14.0: 0.12682234020148653,
        17.0: 0.59855327701641903, 19.0: -0.056821143621433257, 20.0: 0.74715464784363106}
ENUC = 1.1386276671  # nuclear repulsion energy for HeH+ -- constant
EN = -3.99300007772  # SCF energy
####################################################
#
#  CONVERT SPATIAL TO SPIN ORBITAL MO
#
####################################################

# This makes the spin basis double bar integral (physicists' notation)

spinints = np.zeros((dim*2, dim*2, dim*2, dim*2))
for p in range(1, dim*2+1):
    for q in range(1, dim*2+1):
        for r in range(1, dim*2+1):
            for s in range(1, dim*2+1):
                value1 = teimo((p+1)//2, (r+1)//2, (q+1)//2,
                               (s+1)//2) * (p % 2 == r % 2) * (q % 2 == s % 2)
                value2 = teimo((p+1)//2, (s+1)//2, (q+1)//2,
                               (r+1)//2) * (p % 2 == s % 2) * (q % 2 == r % 2)
                spinints[p-1, q-1, r-1, s-1] = value1 - value2

#####################################################
#
#  Spin basis fock matrix eigenvalues
#
#####################################################

fs = np.zeros((dim*2))
for i in range(0, dim*2):
    fs[i] = E[i//2]
fs = np.diag(fs)  # put MO energies in diagonal array

#######################################################
#
#   CCSD CALCULATION
#
#######################################################
dim = dim*2  # twice the dimension of spatial orbital

# Init empty T1 (ts) and T2 (td) arrays

ts = np.zeros((dim, dim))
td = np.zeros((dim, dim, dim, dim))

# Initial guess T2 --- from MP2 calculation!

for a in range(Nelec, dim):
    for b in range(Nelec, dim):
        for i in range(0, Nelec):
            for j in range(0, Nelec):
                td[a, b, i, j] += spinints[i, j, a, b] / \
                    (fs[i, i] + fs[j, j] - fs[a, a] - fs[b, b])

# Make denominator arrays Dai, Dabij
# Equation (12) of Stanton
Dai = np.zeros((dim, dim))
for a in range(Nelec, dim):
    for i in range(0, Nelec):
        Dai[a, i] = fs[i, i] - fs[a, a]

# Stanton eq (13)
Dabij = np.zeros((dim, dim, dim, dim))
for a in range(Nelec, dim):
    for b in range(Nelec, dim):
        for i in range(0, Nelec):
            for j in range(0, Nelec):
                Dabij[a, b, i, j] = fs[i, i] + fs[j, j] - fs[a, a] - fs[b, b]

# Stanton eq (9)


def taus(a, b, i, j):
    taus = td[a, b, i, j] + 0.5*(ts[a, i]*ts[b, j] - ts[b, i]*ts[a, j])
    return taus

# Stanton eq (10)


def tau(a, b, i, j):
    tau = td[a, b, i, j] + ts[a, i]*ts[b, j] - ts[b, i]*ts[a, j]
    return tau

# We need to update our intermediates at the beginning, and
# at the end of each iteration. Each iteration provides a new
# guess at the amplitudes T1 (ts) and T2 (td), that *hopefully*
# converges to a stable, ground-state, solution.


def updateintermediates(x):
    if x == True:
        # Stanton eq (3)
        Fae = np.zeros((dim, dim))
        for a in range(Nelec, dim):
            for e in range(Nelec, dim):
                Fae[a, e] = (1 - (a == e))*fs[a, e]
                for m in range(0, Nelec):
                    Fae[a, e] += -0.5*fs[m, e]*ts[a, m]
                    for f in range(Nelec, dim):
                        Fae[a, e] += ts[f, m]*spinints[m, a, f, e]
                        for n in range(0, Nelec):
                            Fae[a, e] += -0.5 * \
                                taus(a, f, m, n)*spinints[m, n, e, f]

        # Stanton eq (4)
        Fmi = np.zeros((dim, dim))
        for m in range(0, Nelec):
            for i in range(0, Nelec):
                Fmi[m, i] = (1 - (m == i))*fs[m, i]
                for e in range(Nelec, dim):
                    Fmi[m, i] += 0.5*ts[e, i]*fs[m, e]
                    for n in range(0, Nelec):
                        Fmi[m, i] += ts[e, n]*spinints[m, n, i, e]
                        for f in range(Nelec, dim):
                            Fmi[m, i] += 0.5 * \
                                taus(e, f, i, n)*spinints[m, n, e, f]

        # Stanton eq (5)
        Fme = np.zeros((dim, dim))
        for m in range(0, Nelec):
            for e in range(Nelec, dim):
                Fme[m, e] = fs[m, e]
                for n in range(0, Nelec):
                    for f in range(Nelec, dim):
                        Fme[m, e] += ts[f, n]*spinints[m, n, e, f]

        # Stanton eq (6)
        Wmnij = np.zeros((dim, dim, dim, dim))
        for m in range(0, Nelec):
            for n in range(0, Nelec):
                for i in range(0, Nelec):
                    for j in range(0, Nelec):
                        Wmnij[m, n, i, j] = spinints[m, n, i, j]
                        for e in range(Nelec, dim):
                            Wmnij[m, n, i, j] += ts[e, j]*spinints[m,
                                                                   n, i, e] - ts[e, i]*spinints[m, n, j, e]
                            for f in range(Nelec, dim):
                                Wmnij[m, n, i, j] += 0.25 * \
                                    tau(e, f, i, j)*spinints[m, n, e, f]

        # Stanton eq (7)
        Wabef = np.zeros((dim, dim, dim, dim))
        for a in range(Nelec, dim):
            for b in range(Nelec, dim):
                for e in range(Nelec, dim):
                    for f in range(Nelec, dim):
                        Wabef[a, b, e, f] = spinints[a, b, e, f]
                        for m in range(0, Nelec):
                            Wabef[a, b, e, f] += -ts[b, m]*spinints[a,
                                                                    m, e, f] + ts[a, m]*spinints[b, m, e, f]
                            for n in range(0, Nelec):
                                Wabef[a, b, e, f] += 0.25 * \
                                    tau(a, b, m, n)*spinints[m, n, e, f]

        # Stanton eq (8)
        Wmbej = np.zeros((dim, dim, dim, dim))
        for m in range(0, Nelec):
            for b in range(Nelec, dim):
                for e in range(Nelec, dim):
                    for j in range(0, Nelec):
                        Wmbej[m, b, e, j] = spinints[m, b, e, j]
                        for f in range(Nelec, dim):
                            Wmbej[m, b, e, j] += ts[f, j]*spinints[m, b, e, f]
                        for n in range(0, Nelec):
                            Wmbej[m, b, e, j] += -ts[b, n]*spinints[m, n, e, j]
                            for f in range(Nelec, dim):
                                Wmbej[m, b, e, j] += - \
                                    (0.5*td[f, b, j, n] + ts[f, j]
                                     * ts[b, n])*spinints[m, n, e, f]

        return Fae, Fmi, Fme, Wmnij, Wabef, Wmbej

# makeT1 and makeT2, as they imply, construct the actual amplitudes necessary for computing
# the CCSD energy (or computing an EOM-CCSD Hamiltonian, etc)

# Stanton eq (1)


def makeT1(x, ts, td):
    if x == True:
        tsnew = np.zeros((dim, dim))
        for a in range(Nelec, dim):
            for i in range(0, Nelec):
                tsnew[a, i] = fs[i, a]
                for e in range(Nelec, dim):
                    tsnew[a, i] += ts[e, i]*Fae[a, e]
                for m in range(0, Nelec):
                    tsnew[a, i] += -ts[a, m]*Fmi[m, i]
                    for e in range(Nelec, dim):
                        tsnew[a, i] += td[a, e, i, m]*Fme[m, e]
                        for f in range(Nelec, dim):
                            tsnew[a, i] += -0.5*td[e, f, i, m] * \
                                spinints[m, a, e, f]
                        for n in range(0, Nelec):
                            tsnew[a, i] += -0.5*td[a, e, m, n] * \
                                spinints[n, m, e, i]
                for n in range(0, Nelec):
                    for f in range(Nelec, dim):
                        tsnew[a, i] += -ts[f, n]*spinints[n, a, i, f]
                tsnew[a, i] = tsnew[a, i]/Dai[a, i]
    return tsnew

# Stanton eq (2)


def makeT2(x, ts, td):
    if x == True:
        tdnew = np.zeros((dim, dim, dim, dim))
        for a in range(Nelec, dim):
            for b in range(Nelec, dim):
                for i in range(0, Nelec):
                    for j in range(0, Nelec):
                        tdnew[a, b, i, j] += spinints[i, j, a, b]
                        for e in range(Nelec, dim):
                            tdnew[a, b, i, j] += td[a, e, i, j] * \
                                Fae[b, e] - td[b, e, i, j]*Fae[a, e]
                            for m in range(0, Nelec):
                                tdnew[a, b, i, j] += -0.5*td[a, e, i, j]*ts[b, m] * \
                                    Fme[m, e] + 0.5*td[b, e, i, j] * \
                                    ts[a, m]*Fme[m, e]
                                continue
                        for m in range(0, Nelec):
                            tdnew[a, b, i, j] += -td[a, b, i, m] * \
                                Fmi[m, j] + td[a, b, j, m]*Fmi[m, i]
                            for e in range(Nelec, dim):
                                tdnew[a, b, i, j] += -0.5*td[a, b, i, m]*ts[e, j] * \
                                    Fme[m, e] + 0.5*td[a, b, j, m] * \
                                    ts[e, i]*Fme[m, e]
                                continue
                        for e in range(Nelec, dim):
                            tdnew[a, b, i, j] += ts[e, i]*spinints[a,
                                                                   b, e, j] - ts[e, j]*spinints[a, b, e, i]
                            for f in range(Nelec, dim):
                                tdnew[a, b, i, j] += 0.5 * \
                                    tau(e, f, i, j)*Wabef[a, b, e, f]
                                continue
                        for m in range(0, Nelec):
                            tdnew[a, b, i, j] += -ts[a, m]*spinints[m,
                                                                    b, i, j] + ts[b, m]*spinints[m, a, i, j]
                            for e in range(Nelec, dim):
                                tdnew[a, b, i, j] += td[a, e, i, m]*Wmbej[m, b,
                                                                          e, j] - ts[e, i]*ts[a, m]*spinints[m, b, e, j]
                                tdnew[a, b, i, j] += -td[a, e, j, m]*Wmbej[m, b,
                                                                           e, i] + ts[e, j]*ts[a, m]*spinints[m, b, e, i]
                                tdnew[a, b, i, j] += -td[b, e, i, m]*Wmbej[m, a,
                                                                           e, j] + ts[e, i]*ts[b, m]*spinints[m, a, e, j]
                                tdnew[a, b, i, j] += td[b, e, j, m]*Wmbej[m, a,
                                                                          e, i] - ts[e, j]*ts[b, m]*spinints[m, a, e, i]
                                continue
                            for n in range(0, Nelec):
                                tdnew[a, b, i, j] += 0.5 * \
                                    tau(a, b, m, n)*Wmnij[m, n, i, j]
                                continue
                        tdnew[a, b, i, j] = tdnew[a, b, i, j]/Dabij[a, b, i, j]
        return tdnew

# Expression from Crawford, Schaefer (2000)
# DOI: 10.1002/9780470125915.ch2
# Equation (134) and (173)
# computes CCSD energy given T1 and T2


def ccsdenergy():
    ECCSD = 0.0
    for i in range(0, Nelec):
        for a in range(Nelec, dim):
            ECCSD += fs[i, a]*ts[a, i]
            for j in range(0, Nelec):
                for b in range(Nelec, dim):
                    ECCSD += 0.25*spinints[i, j, a, b]*td[a, b, i, j] + \
                        0.5*spinints[i, j, a, b]*(ts[a, i])*(ts[b, j])
    return ECCSD


# ================
# MAIN LOOP
# CCSD iteration
# ================
ECCSD = 0
DECC = 1.0
while DECC > 0.000000001:  # arbitrary convergence criteria
    OLDCC = ECCSD
    Fae, Fmi, Fme, Wmnij, Wabef, Wmbej = updateintermediates(True)
    tsnew = makeT1(True, ts, td)
    tdnew = makeT2(True, ts, td)
    ts = tsnew
    td = tdnew
    ECCSD = ccsdenergy()
    DECC = abs(ECCSD - OLDCC)

print("E(corr,CCSD) = ", ECCSD)
print("E(CCSD) = ", ECCSD + ENUC + EN)
