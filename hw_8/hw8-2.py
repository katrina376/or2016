# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:02:46 2016
@author: Albert Chen
Purpose: To provide students in the OR class a way to visualize kmedoids

Modified by H.-Y. Chan for HW8-2
"""

import numpy as np

import matplotlib.pyplot as plt

import random as rd

from gurobipy import *

import time

start_time = time.time()

N = 500 # 500 points will take about 10 minutes...
K = 2 # do not use K more than 7 or else cannot plot

pts = pt = np.array([[rd.random(),rd.random()] for i in range(N) ])

cij = [[0 for x in range(N)] for y in range(N)]

for i in range(N):
    for j in range(i+1,N):
        cij[i][j] = (
                      (pts[i][0]-pts[j][0])**2
                    + (pts[i][1]-pts[j][1])**2
                    )**0.5
        cij[j][i] = cij[i][j]


m = Model('kmedoids')

xij = {}
for i in range(N):
    for j in range(N):
        xij[i,j] = m.addVar(vtype=GRB.BINARY, obj=cij[i][j],
                               name='x_%d_%d' % (i, j))

m.update()

# first set of constraint
for i in range(N):
    m.addConstr(quicksum(xij[i,j] for j in range(N)) == 1)

# second set of constraint
# strong formulation
for j in range(N):
    for i in range(N):
        m.addConstr(xij[i,j] <= xij[j,j])

# third set of constraint
m.addConstr(quicksum(xij[j,j] for j in range(N)) <= K)


time_gen = time.time() - start_time


start_time = time.time()

m.optimize()

time_sol = time.time() - start_time

color = ['r','g','b','m','c','y','k']

medoidColor = {}

nodeColor = np.chararray((N, 1))

if m.status == GRB.Status.OPTIMAL:
    solution = m.getAttr('x', xij)
    print('node -> medoid' )

    c = 0
    for j in range(N):
        if solution[j,j] > 0:
            medoidColor[j] = color[c]
            c = c + 1


    for i in range(N):
         for j in range(N):
            if solution[i,j] > 0:
                print(' x%d%d -> x%d%d' % (i, j, j, j))
                nodeColor[i] = medoidColor[j]


nodeColor = nodeColor.tostring()

for i in range(N):
    if solution[i,i] > 0:
        plt.plot(pts[i][0], pts[i][1], color=nodeColor[i],marker='x')
    else:
        plt.plot(pts[i][0], pts[i][1], color=nodeColor[i],marker='.')

print("--- Model generation time: %s seconds ---" % (time_gen))
print("--- Model solution time: %s seconds ---" % (time_sol))

plt.show()
