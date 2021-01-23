import math

style = ('Courier', 20, 'italic') 

def squared(x):
  return x * x

def start(board, turtle):
  board.reset()
  # Given Side, solve for Area and Perimeter
  turtle.title("Trapezoid")

  a = board.screen.numinput("Given", "Enter a")
  b = board.screen.numinput("Given", "Enter b")
  h = board.screen.numinput("Given", "Enter h")

  board.home()
  board.forward(b)
  board.left(150)
  board.forward()

  board.goto(-250, 100)
  board.write('a = {}'.format(a), font=style, align='left')
  board.goto(-250, 80)
  board.write('b = {}'.format(b), font=style, align='left')
  board.goto(-250, 60)
  board.write('h = {}'.format(b), font=style, align='left')