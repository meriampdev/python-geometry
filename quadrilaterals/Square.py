import math

style = ('Courier', 20, 'italic') 

def squared(x):
  return x * x

def start(board, turtle):
  board.reset()
  # Given Side, solve for Area and Perimeter
  turtle.title("Square")

  a = board.screen.numinput("Given", "Enter Side")

  board.home()
  board.forward(a)
  board.left(90)
  board.forward(a)
  board.left(90)
  board.forward(a)
  board.left(90)
  board.forward(a)

  # draw diagonal
  c = math.sqrt(squared(a) + squared(a)) # length of the diagonal of course
  board.home() # pen at (0,0)
  board.left(45) # directing pen at 45 degrees for the diagonal
  board.forward(c) 
  # stop drawing
  board.penup()

  baseCenter = (a/2)
  board.goto(baseCenter, -20) #  y at -20 units writes outside the triangle
  board.write('a', font=style, align='left') # a label at the base

  board.goto((a + 10), baseCenter) # writes outside the square 
  board.write('a', font=style, align='left') # a label, right side

  board.goto(baseCenter, (a + 10)) # writes outside the square 
  board.write('a', font=style, align='left') # a label, top side

  board.goto(-20, baseCenter) # writes outside the square 
  board.write('a', font=style, align='left') # a label, left side

  # im sure you kids can follow the other examples and do the write label stuff
  # think of the board as a quadrant (not sure about the term, i forgot.. college was almost 6 years ago for me na)
  # it's just a bunch of coordinates and stuff.. you can figure it out

  board.goto(-250, 100)
  board.write('a = {}'.format(a), font=style, align='left')
  board.goto(-250, 80)
  Area = squared(a)
  board.write('Area = {:.2f}'.format(Area), font=style, align='left')
  board.goto(-250, 60)
  Perimeter = a * 4
  board.write('Perimeter = {}'.format(Perimeter), font=style, align='left')