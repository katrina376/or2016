# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 10:24:31 2016
@author: Albert Chen
Purpose: To provide students in the OR class a skeleton for LR
"""

import numpy as np
import matplotlib.pyplot as plt
import random as rd
from gurobipy import *
import time

def calObjFromSol(candidateXij, cij):
    z_feasible = 0

    for i in range(N):
        if candidateXij[i] <= 0.0001:
            candidate = np.multiply(candidateXij,cij[i,:])
            if np.size(candidate[candidate>0]) > 0:
                z_feasible = z_feasible + np.min(candidate[candidate>0])
            else:
                z_feasible = np.inf
                break
        else:
            z_feasible = z_feasible + cij[i,i]
    return z_feasible



start_time = time.time()

N = 30
K = 3

pts = pt = np.array([[rd.random(),rd.random()] for i in range(N) ])

cij = [[0 for x in range(N)] for y in range(N)]

for i in range(N):
    for j in range(i+1,N):
        cij[i][j] = (
                      (pts[i][0]-pts[j][0])**2
                    + (pts[i][1]-pts[j][1])**2
                    )**0.5
        cij[j][i] = cij[i][j]

cij = np.array(cij)

m = Model('kmedoids')

m.setParam( 'OutputFlag', False )

xij = {}
for i in range(N):
    for j in range(N):
        xij[i,j] = m.addVar(vtype=GRB.BINARY, obj=cij[i][j],
                               name='x_%d_%d' % (i, j))

#m.params.TimeLimit = 20

m.update()

# second set of constrint  ----------------------------
# fill in constrint

# third set of constrint  ----------------------------
# fill in constrint

time_gen = time.time() - start_time

start_time = time.time()

# Lagrangian Relaxation settings
ui = np.zeros(N)
lambda_k = 2
SHRINK = 2     # if obj val do not improve in SHRINK steps, cut lambda_k in half
targer_gap = 1 # percentage
LR_MAX_ITE = 100

# generate a random feasible solution
candidatexjj = np.array([0] * (N-K) + [1] * K)
np.random.shuffle(candidatexjj)
z_feasible = calObjFromSol(candidatexjj, cij)
print 'Random feasible objective value: ', z_feasible

cur_gap = 100
noBetter = 0
z_pre = 0

for ite in range(LR_MAX_ITE):
    # set objective of Lagrangian Problem ----------------------------
    # fill in obj

    m.optimize()

    sumX = np.zeros(N)
    sumSquare = 0
    feasible = True
    for i in range(N):
        sumXi = 0
        for j in range(N):
            sumXi = sumXi + xij[i,j].x
        if abs(sumXi - 1) < 0.0001:
            feasible = feasible and True
        else:
            feasible = feasible and False
        sumX[i] = sumXi
        sumSquare = sumSquare + (1 - sumXi)**2

    # termination condition 1: feasible solution
    if feasible:
        z_feasible = m.objval
        print 'feasible'
        print 'current gap: 0'
        break

    # check obj value if current solution is converted to feasible solution
    for i in range(N):
        candidatexjj[i] = xij[i,i].x
    z_feasible_candidate = calObjFromSol(candidatexjj, cij)

    if z_feasible > z_feasible_candidate:
        z_feasible = z_feasible_candidate
        print 'better feasible found'

    # calculate current gap
    cur_gap = 100*(z_feasible - m.objval)/z_feasible
    print 'current gap: ', cur_gap

    # termination condition 2: current_gap within desired bound
    if cur_gap <= targer_gap:
        print 'smaller than desired gap'
        break

    # update t_k  ----------------------------
    # fill in for this update

    # update lambda_k
    if m.objval < z_pre:
        noBetter = noBetter + 1
    else:
        z_pre = m.objval
        noBetter = 0

    if noBetter >= SHRINK:
        lambda_k = lambda_k / 2.0
        noBetter = 0

    # update ui  ----------------------------
    # fill in for this update

if ite + 1 == LR_MAX_ITE:
    print 'Maximum iteraiton reached'

time_sol = time.time() - start_time

print("--- Model generation time: %s seconds ---" % (time_gen))
print("--- Model solution time: %s seconds ---" % (time_sol))
