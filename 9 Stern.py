from gturtle import *

def onMouseHit(x, y):
    fill(x, y)      
        
makeTurtle(mouseHit = onMouseHit)
hideTurtle()
addStatusBar(30)
setStatusText("Click to fill a region!")
  
repeat 9:
    fd(300)
    rt(160)
