import math

style = ('Courier', 20, 'italic') 

def squared(x):
  return x * x

def start(board, turtle):
  board.reset()
  # Given Side, solve for Area and Perimeter
  turtle.title("Rectangle")

  l = board.screen.numinput("Given", "Enter Length")
  w = board.screen.numinput("Given", "Enter Width")

  board.home()
  board.forward(l) # drawing base
  board.left(90)
  board.forward(w) # draw right side
  board.left(90)
  board.forward(l) # draw top side
  board.left(90)
  board.forward(w) # draw left side 
  board.penup()

  board.goto(-250, 100)
  board.write('l = {}'.format(l), font=style, align='left')
  board.goto(-250, 80)
  board.write('w = {}'.format(w), font=style, align='left')
  board.goto(-250, 60)
  Area = l * w
  board.write('Area = {:.2f}'.format(Area), font=style, align='left')
  board.goto(-250, 40)
  Perimeter = 2 * (l+w)
  board.write('Perimeter = {}'.format(Perimeter), font=style, align='left')

  # you kids can do the rest, im sure
  