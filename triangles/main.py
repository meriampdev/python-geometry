import turtle
import Equilateral
import RightTriangle
import Isosceles
# Triangles: equilateral triangle, right triangle, isosceles triangle, 30-60-90

board = turtle.Turtle()

def start():
  inputString = """Press
    "'e' for Equilateral Triangle
    "'r' for Right Triangle
    "'i' for Isosceles Triangle
    "'qq' to Quit
    "- """

  userInput = str(input(inputString))
  while userInput != 'qq':
    if userInput == 'e':
      Equilateral.start(board, turtle)
    elif userInput == 'r':
      RightTriangle.start(board, turtle)
    elif userInput == 'i':
      Isosceles.start(board, turtle)
    else:
      pass

    userInput = str(input(inputString))

start()