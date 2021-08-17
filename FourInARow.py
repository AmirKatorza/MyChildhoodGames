from collections import defaultdict
import random as rd

def create_board(rows=6, columns=7):
   board = [[' ' for c in range(columns)] for r in range(rows)]
   return board

def print_board(board):
  for r in board:
    print(r)
  print("\n")  

def get_free_cells(board):
   free_cells = [] 
   for i, row in enumerate(board):
     for j, col in enumerate(row):
       if (col == ' '):
         free_cells.append((j, i))
   d = defaultdict(list)
   for k, v in free_cells:
     d[k].append(v) 
   sorted(d.items())
   return d

def max_sequence(board, cell, player):
  if (player != 'X') and (player != 'O'):
    return 0
  if (cell[0] < 0 or cell[0] >= len(board[0]) or cell[1] < 0 or cell[1] >= len(board)):
       return 0
      
  row = cell[0]
  col = cell[1]

  # horizontal
  right, left = col + 1, col - 1
  max_horizontal = 1
  while (left >= 0 and board[row][left] == player):
    left -= 1
    max_horizontal += 1
  while (right < len(board) and board[row][right] == player):
    right += 1
    max_horizontal += 1

  # vertical
  up, down = row + 1, row - 1
  max_vertical = 1
  while (down >= 0 and board[down][row] == player):
    down -= 1
    max_vertical += 1
  while (up < len(board) and board[up][col] == player):
    up += 1
    max_vertical += 1

  # primary diagonal
  up_row = row - 1
  down_row = row + 1
  left_col = col - 1
  right_col = col + 1
  max_primary_diagonal = 1
  while (up_row >=0 and left_col >=0 and board[up_row][left_col] == player):
      up_row -= 1
      left_col -= 1
      max_primary_diagonal += 1
      
  while (down_row < len(board) and right_col < len(board) and board[down_row][right_col] == player):
      down_row += 1
      right_col += 1
      max_primary_diagonal +=1

  # secondary Diagonal
  up_row = row - 1
  down_row = row + 1
  left_col = col - 1
  right_col = col + 1
  max_secondary_diagonal = 1
  while (up_row >=0 and right_col < len(board) and board[up_row][right_col] == player):
      up_row -= 1
      right_col += 1
      max_secondary_diagonal += 1

  while (down_row < len(board) and left_col >= 0 and board[down_row][left_col] == player):
      down_row +=1 
      left_col -=1 
      max_secondary_diagonal += 1
  
  return max(max_horizontal, max_vertical, max_primary_diagonal, max_secondary_diagonal)
        
def check_victory(board, player):
  for i, row in enumerate(board):
    for j, col in enumerate(row):
      if col == player:
        cell = (i, j)
        if (max_sequence(board, cell, player)  >= 4):
          return True
  return False

def make_move(board, player, player2):
  free_cells = get_free_cells(board)
  print(f"This is player {player} turn")
  if (player == 'X'):
    get_col = int(input(f"Please choose a column: must be a number between 0 to {len(board)-1}: \n"))
    while not get_col in free_cells.keys():
      get_col = int(input("Illegal move - Choose a valid or free column: "))
    board[max(free_cells[get_col])][get_col] = 'X'
      
  elif (player == 'O' and player2 == 0):
    get_col = int(input(f"Please choose a column: must be a number between 0 to {len(board)-1}: \n"))
    while not get_col in free_cells.keys():
      get_col = int(input("Illegal move - Choose a valid or free column: "))
    board[max(free_cells[get_col])][get_col] = 'O'
  
  else:
    print("The Computer is now playing\n")
    get_col = rd.choice(list(free_cells.keys()))
    board[max(free_cells[get_col])][get_col] = 'O'
  
def play_4connect():
  
  print("Welcome to 4 connect game\n")

  player2_choise = int(input("Who would you like to play against:\n0-human player\n1-computer\n"))
  while (player2_choise != 0) and (player2_choise != 1):
    print("Invalid number, please try again")
    player2_choise = int(input("Who would you like to play against:\n0-human player\n1-computer\n"))

  num_of_rows = int(input("Please enter number of rows: "))
  num_of_cols = int(input("Please enter number of columns: "))


  board = create_board(num_of_rows, num_of_cols)
  print_board(board)

  last_player = 'O'
  while (get_free_cells(board) and not check_victory(board, last_player)):
    if (last_player == 'X'): 
      last_player = 'O' 
    else:
      last_player = 'X'
    make_move(board, last_player, player2_choise)
    print_board(board)

  if (check_victory(board, last_player)):
    print(f"player {last_player} Wins!!!")
  else:
    print("Draw - Nobody Won... :( !!!")