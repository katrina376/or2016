import numpy as np
from gurobipy import *

def show_state(_v1,_v2,im):
    print '======'
    print('v1 = %f' %_v1)
    print('v2 = %f' %_v2)
    if (im.getAttr('Status') > 2) :
        print 'Infeasible'
        return

    for v in im.getVars():
        print('%s = %f' % (v.varName, v.x))
    print('zd = %f' % m.objVal)

m = Model('hw9-1')
m.setParam('OutputFlag', False)

x1 = m.addVar(name='x1',vtype=GRB.BINARY)
x2 = m.addVar(name='x2',vtype=GRB.BINARY)
x3 = m.addVar(name='x3',vtype=GRB.BINARY)
x4 = m.addVar(name='x4',vtype=GRB.BINARY)

v1 = 0.0 #m.addVar(name='v1')
v2 = 0.0 #m.addVar(name='v2')

m.update()

m.setObjective(16 * x1 + 10 * x2 + 4 * x4 + v1 * (1 - x1 - x2) + v2 * (1 - x3 - x4), GRB.MAXIMIZE)
m.addConstr(8 * x1 + 2 * x2 + x3 + 4 * x4 <= 10)
m.optimize()

z_feasible = 0

while abs((m.objVal - z_feasible) / m.objVal) > 0.001:
    show_state(v1,v2,m)

    x1_f = x1.x
    x2_f = x2.x
    x3_f = x3.x
    x4_f = x4.x

    if ((8 * x1_f + 2 * x2_f + x3_f + 4 * x4_f <= 10) & (x1_f + x2_f <= 1) & (x3_f + x4_f <= 1)):
        z_feasible = 16 * x1_f + 10 * x2_f + 4 * x4_f
    print('z_feasible = %f' %z_feasible)

    tk_v1 = 1 * (m.objVal - z_feasible) / ((1 - x1_f - x2_f)**2 + (1 - x3_f - x4_f)**2)
    tk_v2 = 1 * (m.objVal - z_feasible) / ((1 - x1_f - x2_f)**2 + (1 - x3_f - x4_f)**2)

    v1 = max(0, v1 - tk_v1 * (1 - x1_f - x2_f)) #m.addVar(name='v1')
    v2 = max(0, v2 - tk_v2 * (1 - x3_f - x4_f)) #m.addVar(name='v2')
    m.setObjective(16 * x1 + 10 * x2 + 4 * x4 + v1 * (1 - x1 - x2) + v2 * (1 - x3 - x4), GRB.MAXIMIZE)
    m.optimize()
