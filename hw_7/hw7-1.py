from gurobipy import *

def show_state(im):
  print '======'
  if (im.getAttr('Status') > 2) :
    print 'Infeasible'
    return
    
  for v in im.getVars():
    print('%s = %f' % (v.varName, v.x))
  print('z = %f' % m.objVal)

m = Model("hw7-1")
m.setParam('OutputFlag', False)

x1 = m.addVar(name='x1')
x2 = m.addVar(name='x2')

m.update()

m.setObjective(8 * x1 + 5 * x2, GRB.MAXIMIZE)
m.addConstr(x1 + x2 <= 6, 'constraint 1')
m.addConstr(9 * x1 + 5 * x2 <= 45, 'constraint 2')

# Root
m.optimize()
show_state(m)

# Split by x1 = 3.75
# 1st
# Branch on Left
constr1 = m.addConstr(x1 <= 3, '1st LHS')
m.optimize()
show_state(m)
# z = 39, z_curlow = 39
# Stop at x1 = 3, x2 = 3

# Branch on Right
m.remove(constr1)
constr1 = m.addConstr(x1 >= 4, '1st RHS')
m.optimize()
show_state(m)
# z = 41

# Split by x2 = 1.8
# 2nd
# Branch on Left
constr2 = m.addConstr(x2 <= 1, '2nd LHS of 1st RHS')
m.optimize()
show_state(m)
# z = 40.56

# Split by x1 = 4.4444
# 3rd
# Branch on Left
constr3 = m.addConstr(x1 <= 4, '3rd LHS of 2nd LHS')
m.optimize()
show_state(m)
# z = 37 < z_curlow = 39, z_curlow = 37
# Stop at x1 = 4, x2 = 1

# Branch on Right
m.remove(constr3)
constr3 = m.addConstr(x1 >= 5, '3rd RHS of 2nd LHS')
m.optimize()
show_state(m)
# z = 40
# Stop at x1 = 5, x2 = 0

# Back to 2nd
# Branch on Right
m.remove(constr3)
m.remove(constr2)
constr2 = m.addConstr(x2 >= 2, '2nd RHS of 1st RHS')
m.optimize()
show_state(m)
# Infeasible or unbounded
# Stop

# z_opt = 40 at x1 = 5, x2 = 0
