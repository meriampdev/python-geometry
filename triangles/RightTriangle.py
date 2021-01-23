import turtle
import math

def squared(x):
  return x * x

def start(board, turtle):
  board.reset()
  turtle.title("Right Triangle")

  a = board.screen.numinput("a", "Leg a")
  b = board.screen.numinput("a", "Leg b")

  board.home()
  board.left(90)
  board.forward(a)
  board.home()
  board.forward(b)
  
  # calculate hypotenuse
  # angles and stuff.. refer to isosceles.. ask me if naai di klaro
  # im very sleepy na 