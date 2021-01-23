import math

# CONSTANT
style = ('Courier', 20, 'italic') 

def squared(x):
  return x * x

def start(board, turtle):
  board.reset()
  turtle.title("Isosceles Triangle")

  base = board.screen.numinput("Given", "Enter Base")
  height = board.screen.numinput("Given", "Enter Height")
  Area = (base*height) / 2

  # Explore 
  # para maka render mo
  # isosceles triangle, 30-60-90
  # ask questions

  # given height and base,
  # measure one side using formula for hypotenuse
  # c = (you know the rest)
  # a = height, b = base/2 
  c = math.sqrt((squared(height) + squared(base/2)))
  side = c
  Perimeter = (2 * side) + base

  board.home()
  board.forward(base) # draw base
  
  # let's find the angle asa padung ang drawing after sa base
  # α = asin(a / c)
  angle1 = math.degrees(math.asin(height/side))
  angle2 = 180 - angle1 # im sure you can figure out the why of 180 - angle1
  board.left(angle2)
  board.forward(side)
  board.penup()
  board.home()
  board.pendown()
  board.left(angle1)
  board.forward(side)
  board.penup()
  
  baseCenter = (base/2)
  board.home()
  board.goto(baseCenter, 0) # we're pointing the pen at this very coordinate
  board.pendown()
  board.left(90)
  board.forward(height)
  board.penup()

  board.goto(baseCenter, -20) #  y at -20 units writes outside the triangle
  board.write('a = {:.2f}'.format(side), font=style, align='left')

  board.goto((baseCenter + 10), (height/2))
  board.write('h = {}'.format(height), font=('Courier', 15, 'italic') , align='left')

  board.goto(-250, 120)
  board.write('Given:', font=style, align='left')
  board.goto(-250, 100)
  board.write('b = {}'.format(base), font=style, align='left')
  board.goto(-250, 80)
  board.write('h = {}'.format(height), font=style, align='left')
  board.goto(-250, 60)
  board.write('Calculate', font=style, align='left')
  board.goto(-250, 40)
  board.write('Area = {:.2f}'.format(Area), font=style, align='left')
  board.goto(-250, 20)
  board.write('Perimeter = {:.2f}'.format(Perimeter), font=style, align='left')