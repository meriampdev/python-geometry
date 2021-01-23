import math

style = ('Courier', 20, 'italic') 

def squared(x):
  return x * x

def start(board, turtle):
  board.reset()
  # Given Side, solve for Area and Perimeter
  turtle.title("Rhombus")

  p = board.screen.numinput("Given", "Enter P diagonal")
  q = board.screen.numinput("Given", "Enter Q diagonal")

  board.home() # you know the drill, set the pen at (0,0)
  # draw the q
  board.forward(q)
  qCenter = q/2
  pCenter = p/2 # or half of p 

  board.penup()
  board.goto(qCenter, 0)
  board.pendown()
  board.left(90)
  board.forward(pCenter) # draw half of p upwards
  board.left(180) # point pen downwards
  board.forward(p) # draw the whole line
  board.penup()
  # calculate sides
  # using our good old friend hypotenuse of course
  side = math.sqrt(squared(pCenter) + squared(qCenter))
  
  board.goto(qCenter, (-1 * pCenter))
  board.pendown()

  # quadrant 4 triangle angles
  q4bAngle = math.degrees(math.acos(pCenter/side))
  q4aAngle = 90 - q4bAngle
  penAngle = 90 + (90 - q4bAngle)
  board.left(penAngle)
  board.forward(side)

  # quadrant 1 triangle angles
  q1aAngle = math.degrees(math.atan(pCenter/qCenter))
  penAngle = 90 + (90 - (q4aAngle + q1aAngle))
  board.left(penAngle)
  board.forward(side)

  # quadrant 2 triangle angles
  penAngle = 90 - (90 - (q4aAngle + q1aAngle))
  board.left(penAngle)
  board.forward(side)

  # quadrant 3 triangle angles
  penAngle = 90 + (90 - (q4aAngle + q1aAngle))
  board.left(penAngle)
  board.forward(side)
  board.penup()

  board.goto(-250, 100)
  board.write('p = {}'.format(p), font=style, align='left')
  board.goto(-250, 80)
  board.write('q = {}'.format(q), font=style, align='left')