
def start(board, turtle):
  board.reset()
  # Given Side, solve for Area and Perimeter
  turtle.title("Cube")

  # forming front square face 
  for i in range(4): 
      board.forward(100) 
      board.left(90) 
    
  # bottom left side 
  board.goto(50,50) 
    
  # forming back square face 
  for i in range(4): 
      board.forward(100) 
      board.left(90) 
    
  # bottom right side 
  board.goto(150,50) 
  board.goto(100,0) 
    
  # top right side 
  board.goto(100,100) 
  board.goto(150,150) 
    
  # top left side 
  board.goto(50,150) 
  board.goto(0,100)
