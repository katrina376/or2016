from gurobipy import *
import BBNode as bn
import math

stack = []

m = Model("hw7-bouns")
m.setParam('OutputFlag', False)

dv = {
  'x1' : m.addVar(name='x1'),
  'x2' : m.addVar(name='x2')
}

m.update()

root = bn.BBNode(None, '', '', 0)
m.setObjective(8 * dv['x1'] + 5 * dv['x2'], GRB.MAXIMIZE)
m.addConstr(dv['x1'] + dv['x2'] <= 6, 'constraint 1')
m.addConstr(9 * dv['x1'] + 5 * dv['x2'] <= 45, 'constraint 2')

z_min = 0
feasibles = []
constraints = []
stack.append(root)

while (len(stack) > 0):
  nn = stack.pop()

  if (nn.dv in dv):
    if (nn.boundSense == 'ub'):
      constraints.append(m.addConstr(dv[nn.dv] <= nn.bound))
    else:
      constraints.append(m.addConstr(dv[nn.dv] >= nn.bound))

  m.optimize()

  dvNode = nn
  print '======'
  print 'Showing bounds from current node to root'
  while dvNode != root:
    print dvNode.dv, dvNode.boundSense, dvNode.bound
    dvNode = dvNode.parent

  if (m.getAttr('Status') > 2):
    # STOP for infeasible or unbounded
    print 'Infeasible, stop'
    m.remove(constraints.pop())
  else:
    nn.set_obj(m.objVal)
    print('z = %f' % m.objVal)
    dvSol = {}
    for v in m.getVars():
      dvSol[str(v.varName)] = float(v.x)
      print('%s = %f' %(v.varName, v.x))
    nn.set_dvSol(dict(dvSol))
    nn.set_status(m.getAttr('Status'))
    if (z_min > m.objVal):
      # STOP for z < z_curr_min
      print 'z < z_curr_min, stop'
      m.remove(constraints.pop())
    else:
      # Search for fractional vars
      all_int = True
      for v in m.getVars():
        if (v.x % 1 > 0.000001):
          all_int = False
          print('Branch and Bound on %s = %f' % (v.varName, v.x))
          lc = bn.BBNode(nn, v.varName, 'ub', math.floor(v.x))
          rc = bn.BBNode(nn, v.varName, 'lb', math.ceil(v.x))
          stack.append(lc)
          stack.append(rc)
          has_fractional = False
          break
      if all_int:
        print 'int Solution, stop'
        feasibles.append(nn)
        m.remove(constraints.pop())


opt_idx = 0
z_max = 0

for i in range(0,len(feasibles)):
  if (feasibles[i].obj > z_max):
    z_max = feasibles[i].obj
    opt_idx = i

print '============'
print 'Optimal Solution : '
print('z = %f' % feasibles[opt_idx].obj)
for k,v in feasibles[opt_idx].dvSol.items():
  print('%s : %f' %(k, v))
