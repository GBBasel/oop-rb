from gturtle import *

def onMouseMoved(x, y):
    setHeading(towards(x, y))
    forward(10)
      
makeTurtle(mousePressed = onMouseMoved, mouseDragged = onMouseMoved)
speed(-1)

