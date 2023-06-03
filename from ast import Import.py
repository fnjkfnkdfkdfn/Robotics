from ast import Import


Import ("vcscript")

comp = "getComponent"()
robotController = comp.findBehavioursByType("VC_ROBOTCONTROLLER")[0]

internal_joints = []
for joint in robotController.Joints:
  if joint.ExternalController == None:
    internal_joints.append(joint)
    
external_joints = []
for joint in robotController.Joints:
  if joint.ExternalController != None:
    #print joint.ExternalController
    external_joints.append(joint)

def getInternalJointsInRobot(rc):
  '''Returns a list of joints assigned to a given robot controller
  excluding imported joints'''
  return list(filter(lambda x: x.ExternalController == None,rc.Joints))

def getExternalJointsInRobot(rc):
  '''Returns a list of imported joints assigned to a given robot controller'''
  return list(filter(lambda x: x.ExternalController != None, rc.Joints))

#for joint in getExternalJointsInRobot(robotController):
#  joint.CurrentValue = 500.0

def getAllNodesInComponent(comp, nodes=[], includeRootNode=False):
  '''Returns a list of nodes in a given component
  excluding nodes from other components.
  By default, the list will not include the component root node.
  Otherwise, pass includeRootNode a true value.'''
  if not nodes:
    nodes = []
  
  if includeRootNode == True:
    nodes.append(comp)
    
  for node in comp.Children:
    if node.Component == comp.Component:
      nodes.append(node)
      if node.Children:
        getAllNodesInComponent(node, nodes)
        
  return nodes
  
def getAllDofInComponent(comp):
  '''Returns a list of all DOF objects for a given component
  excluding DOF objects in parent or attached components and
  nodes with a JointType of Fixed.'''
  #list = map(lambda x: x.Dof, getAllNodesInComponent(comp))
  #return filter(lambda x: x != None, list)
  return filter(lambda x: x != None, map(lambda x: x.Dof, getAllNodesInComponent(comp))) 

#for dof in getAllDofInComponent(comp):
#  dof.VALUE = 0
  
#getApplication().render()