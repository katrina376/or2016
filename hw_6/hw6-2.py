from gurobipy import *

# The names of plants and markets
plants = ['P1', 'P2']
markets = ['M1', 'M2', 'M3']

# The supplies of the plants
supplies = {'P1' : 15, 'P2' : 20}

# The demands of the markets
demands = {'M1' : 17, 'M2' : 8, 'M3' : 10}

# The matrix of costs
cost = {('P1','M1') : 3.0,
        ('P1','M2') : 4.0,
        ('P1','M3') : 6.0,
        ('P2','M1') : 5.0,
        ('P2','M2') : 7.0,
        ('P2','M3') : 5.0}

arcs, cost = multidict(cost)

mo = Model("hw6-2")
x = {}

for p, m in arcs:
    x[p, m] = mo.addVar(name='From %s to %s' %(p, m), obj=cost[p, m])

mo.update()

for p in plants:
    mo.addConstr(quicksum(x[p,m] for m in markets) <= supplies[p])

for m in markets:
    mo.addConstr(quicksum(x[p,m] for p in plants) >= demands[m])

mo.optimize()

if mo.status == GRB.Status.OPTIMAL:
    print 'Objective: %f' % mo.ObjVal
    for v in mo.getVars():
        print '%s : %f' %(v.varName, v.x)
