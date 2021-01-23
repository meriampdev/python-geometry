import turtle
import Square
import Rectangle
import Rhombus
import Parallelogram
import Trapezoid

# Quadrilaterals: square, rectangle, rhombus, parallelogram, trapezoid
board = turtle.Turtle()

def start():
  inputString = """Press
    "'s' for Square
    "'rt' for Rectangle
    "'rh' for Rhombus
    "'p' for Parellelogram
    "'t' for Trapezoid
    "'qq' to Quit
    "- """

  userInput = str(input(inputString))
  while userInput != 'qq':
    if userInput == 's':
      Square.start(board, turtle)
    elif userInput == 'rt':
      Rectangle.start(board, turtle)
    elif userInput == 'rh':
      Rhombus.start(board, turtle)
    elif userInput == 'p':
      Parallelogram.start(board, turtle)
    elif userInput == 't':
      Trapezoid.start(board, turtle)
    else:
      pass

    userInput = str(input(inputString))

start()
