import numpy as np
from gurobipy import *

# The names of each node
nodes = ['1', '2', '3', '4', '5', 'home']
subtour_elim_nodes = nodes[0:len(nodes)-1]

# Create Variables
x = {}
u = {}

# The distance matrix C
C = np.array([[   0, 2429, 1967, 1497, 1650, 2392],
              [2429,    0, 1105, 1674, 1320, 5566],
              [1967, 1105,    0, 2023, 9527,  560],
              [1497, 1674, 2023,    0, 1999, 1273],
              [1650, 1320, 9527, 1999,    0,  778],
              [2392, 5566,  560, 1273,  773,    0]])

cost = {}
valid_connects = {}

for i in range(len(C)):
    valid_connects[nodes[i]] = []
    for j in range(len(C[i,:])):
        if i != j:
            cost[nodes[i], nodes[j]] = C[i,j]
            valid_connects[nodes[i]].append(nodes[j])

arcs, cost = multidict(cost)

m = Model("hw6-1")

for n in subtour_elim_nodes:
    u[n] = m.addVar(name='u_%s' %n, obj=0)

for i, j in arcs:
    x[i, j] = m.addVar(name='x_%s%s' %(i, j), obj=cost[i, j], vtype=GRB.BINARY)

m.update()

# Constraints for incomes
for nj in nodes:
    m.addConstr(quicksum(x[ni,nj] for ni in valid_connects[nj]) == 1, 'income_%s' %nj)

# Constraints for outgoes
for ni in nodes:
    m.addConstr(quicksum(x[ni,nj] for nj in valid_connects[ni]) == 1, 'outgo_%s' %ni)

# Constraints for subtours
for i, j in arcs:
    if i in subtour_elim_nodes and j in subtour_elim_nodes:
       m.addConstr(u[i] - u[j] + len(nodes) * x[i, j] <= len(nodes) - 1, 'subtour_%s%s' %(i, j))

m.optimize()

path_dict = {}
path = []

if m.status == GRB.Status.OPTIMAL:
    print 'Objective: %f' % m.ObjVal
    solution = m.getAttr('x', x)
    for i, j in arcs:
        if solution[i,j] > 0:
            print('%s -> %s: %g' % (i, j, solution[i,j]))
            path_dict[i] = j

path.append('home')
prev = path_dict['home']
while prev != 'home':
    path.append(prev)
    prev = path_dict[prev]
path.append(prev)

path_str = str(path[0])
for i in range(1,len(path)):
    path_str += ' -> ' + path[i]

print 'Optimal Path: %s' %path_str
