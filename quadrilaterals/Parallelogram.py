import math

style = ('Courier', 20, 'italic') 

def squared(x):
  return x * x

def start(board, turtle):
  board.reset()
  # Given Side, solve for Area and Perimeter
  turtle.title("Parallelogram")

  a = board.screen.numinput("Given", "Enter a")
  b = board.screen.numinput("Given", "Enter b")

  board.home()
  board.forward(b)

  board.home()
  board.left(60)
  board.forward(a)
  board.right(60)
  board.forward(b)
  board.right(120)
  board.forward(a)
  board.penup()

  baseCenter = (b/2)
  board.goto(baseCenter, -20) #  y at -20 units writes outside the triangle
  board.write('b', font=style, align='left') # a label at the base

  board.goto(-250, 100)
  board.write('a = {}'.format(a), font=style, align='left')
  board.goto(-250, 80)
  board.write('b = {}'.format(b), font=style, align='left')