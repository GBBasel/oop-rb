from gturtle import *

def onMouseHit(x, y):
    fill(x, y)
    
def onMouseMoved(x, y):
    setHeading(towards(x, y))
    forward(10)
      
makeTurtle(mouseHit = onMouseHit, isRightMouseButton = onMouseHit, mouseDragged = onMouseMoved, mousePressed = onMouseMoved, isLeftMouseButton = onMouseMoved)
speed (-1)