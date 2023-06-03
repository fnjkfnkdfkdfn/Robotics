from dis import Positions
from sqlite3.dbapi2 import _Statement
from turtle import position
"from vcscript import*"

comp = "getComponent"()
robotExecutor = comp.findBehaviorsByType("rRobotExecutor") [0]
robotProgram = robotExecutor.Program
mainRoutine = robotProgram.MainRoutine

mainRoutine.clear
for subroutine in robotProgram.Routines:
   robotProgram.deleteRoutine(subroutine)

statments = mainRoutine.addStatment("VC_STATEMENT_PRINT")
_Statement.Message = "Hello World"

statement = mainRoutine.addStatement("VC_STATEMENT_DELAY,0")
"statment".Delay = 2.0

statement = mainRoutine.addstatement("VC_STATEMENT_PTMOTION")
positons = statement.Positions[0]

#pos_matrix = Positions.PositionInWorld
#pos_matrix.translate(1000,0,1000)
#pos_matrix.rotateReLY(180.0)

app = "getAplication"()
cube = app.findComponent("Cube")
cube_center = cube.BoundCenter
"pos_matrix".translateRel(cube_center.X, cube_center.Y, cube_center.z * 2 )
position.PositionInWorld = "pos_matrix"

subroutine= robotProgram.findRoutine("Example ")
if subroutine:
    subroutine.clear()
if not subroutine:
 subroutine= robotProgram.addRoutine("Example ")

statement = "subroutine".addstatement("VC_STATEMENT_PTMOTION")
position = statement.Positions[0]\
(position).PositionInWorld = "pos_matrix" 

