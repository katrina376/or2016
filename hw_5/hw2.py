from gurobipy import *

m = Model("hw2")

x1a = m.addVar(name="From Supply 1 to Warehouse A")
x1b = m.addVar(name="From Supply 1 to Warehouse B")
x1c = m.addVar(name="From Supply 1 to Warehouse C")
x2a = m.addVar(name="From Supply 2 to Warehouse A")
x2b = m.addVar(name="From Supply 2 to Warehouse B")
x2c = m.addVar(name="From Supply 2 to Warehouse C")

ya1 = m.addVar(name="From Warehouse A to Demand 1")
ya2 = m.addVar(name="From Warehouse A to Demand 2")
yb1 = m.addVar(name="From Warehouse B to Demand 1")
yb2 = m.addVar(name="From Warehouse B to Demand 2")
yc1 = m.addVar(name="From Warehouse C to Demand 1")
yc2 = m.addVar(name="From Warehouse C to Demand 2")

w11 = m.addVar(name="From Supply 1 to Demand 1")
w12 = m.addVar(name="From Supply 1 to Demand 2")
w21 = m.addVar(name="From Supply 2 to Demand 1")
w22 = m.addVar(name="From Supply 2 to Demand 2")

za = m.addVar(vtype=GRB.BINARY,name="If Warehouse A is chosen")
zb = m.addVar(vtype=GRB.BINARY,name="If Warehouse B is chosen")
zc = m.addVar(vtype=GRB.BINARY,name="If Warehouse C is chosen")

m.update()

m.setObjective( 1 * x1a +  6 * x2a +  2 * x1b + 3 * x2b + 8 * x1c + 1 * x2c
             +  4 * ya1 +  6 * ya2 +  3 * yb1 + 4 * yb2 + 5 * yc1 + 3 * yc2
             +  4 * w11 +  8 * w12 +  7 * w21 + 6 * w22
             + 50 *  za + 60 *  zb + 68 *  zc, GRB.MINIMIZE)

m.addConstr( x1a + x1b + x1c + w11 + w12 <= 50, "Total supply from 1")
m.addConstr( x2a + x2b + x2c + w21 + w22 <= 75, "Total supply from 2")

m.addConstr( ya1 + yb1 + yc1 + w11 + w21 >= 75, "Total demand to 1")
m.addConstr( ya2 + yb2 + yc2 + w12 + w22 >= 50, "Total demand to 2")

# Capacity limit of A is inf.
m.addConstr( x1b + x2b <= zb * 60, "Capacity limit of B")
m.addConstr( x1c + x2c <= zc * 70, "Capacity limit of C")

m.addConstr( za + zb + zc <= 1, "Chosen warehouse")

m.addConstr( x1a + x2a >= ya1 + ya2, "Continuity of A")
m.addConstr( x1b + x2b >= yb1 + yb2, "Continuity of B")
m.addConstr( x1c + x2c >= yc1 + yc2, "Continuity of C")

m.optimize()

for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))

print('Minimum total cost: %f' % m.objVal)
