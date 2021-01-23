import math

def squared(x):
  return x * x

def start(board, turtle):
  board.reset()
  # Given Side, solve for Area and Perimeter
  turtle.title("Equilateral Triangle")

  a = board.screen.numinput("Given", "Enter Side")
  Area = (math.sqrt(3)/4) * squared(a)
  Perimeter = 3 * a 

  style = ('Courier', 20, 'italic') 
  side = a * 2 # x2 to make the drawing bigger
  
  board.home() # sets the pen at (0,0), notice that drawing starts at the center
  board.forward(side) # draw base, we have the pen at a horizontal direction at this point
  # turn the pen by 120 degress (you can change these values)
  board.left(120)
  # write forward (upward) by (value of side) units
  board.forward(side)
  # turn the pen again by 120 degress, writing on a downward direction
  board.left(120)
  board.forward(side)
  # penup stops drawing
  board.penup()

  baseCenter = (side/2) # i think you kids can figure this one out :D 
  h = side * (math.sqrt(3) / 2) # im sure you kids are also familiar with the formula

  board.home()
  board.goto(baseCenter, 0) # we're pointing the pen at this very coordinate
  board.pendown()
  
  board.left(90)
  board.forward(h) # drawing the line for height here obviously
  board.penup()
  
  # write label for height
  board.goto((baseCenter + 10), (h/2))
  board.write('h = {:.2f}'.format(h), font=('Courier', 15, 'italic') , align='left')

  board.goto(baseCenter, -20) #  y at -20 units writes outside the triangle
  board.write('a', font=style, align='center')

  # try writing the other 'a' for the other sides 
  # of the triangle, 
  # im sure you can figure out the coordinates for that (i can't wa ko kabalo sa formula :P)
  # board.goto(x, y)
  # board.write('a', font=style, align='center')
  
  board.goto(-250, 100)
  board.write('a = {}'.format(a), font=style, align='left')
  board.goto(-250, 80)
  board.write('Area = {:.2f}'.format(Area), font=style, align='left')
  board.goto(-250, 60)
  board.write('Perimeter = {}'.format(Perimeter), font=style, align='left')