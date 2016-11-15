class BBNode(object): 
  def __init__(self, parent, dv, boundSense, bound):
    self.parent = parent
    self.dv = dv
    self.boundSense = boundSense
    self.bound = bound
  
  def set_obj(self, obj):
    self.obj = obj
  
  def set_dvSol(self, dvSol):
    self.dvSol = dvSol
  
  def set_status(self, status):
    self.status = status
