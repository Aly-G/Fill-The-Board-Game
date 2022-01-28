#import libraries
from guizero import App, Waffle, Text, PushButton, info
import random
#variables
colours = ["red", "blue", "green", "yellow", "magenta", "purple"]
difficulty=input("What difficulty level would you like to play? (Easy, Medium, Hard): ")
if difficulty=="Easy":
    board_size=10
    moves_limit=25
elif difficulty=="Medium":
    board_size=15
    moves_limit=30
elif difficulty=="Hard":
    board_size=20
    moves_limit=27
moves_taken=0
#functions
def flood(x, y, target, replacement): #recursively floods adjacent squares
    if target == replacement:
        return False
    if board.get_pixel(x,y) != target:
        return False
    board.set_pixel(x, y, replacement)
    if y+1 <= board_size-1: #south
        flood(x, y+1, target, replacement)
    if y-1 <= 0: #north
        flood(x, y-1, target, replacement)
    if x+1 <= board_size-1: #east
        flood(x+1, y, target, replacement)
    if x-1 >= 0: #west
        flood(x-1, y, target, replacement)

def all_squares_are_the_same():
    squares = board.get_all()
    if all(colour == squares[0] for colour in squares):
        return True
    else:
        return False
    
def win_check():
    global moves_taken
    moves_taken += 1
    if moves_taken <= moves_limit:
        if all_squares_are_the_same():
            win_text.value = "You Win"
    else:
        win_text.value = "You lost"

def fill_board():
    for x in range(board_size):
        for y in range(board_size):
            board.set_pixel(x, y, random.choice(colours))
            
def init_palette():
    for colour in colours:
        palette.set_pixel(colours.index(colour), 0, colour)
        
def start_flood(x, y):
    flood_colour = palette.get_pixel(x,y)
    target = board.get_pixel(0,0)
    flood(0, 0, target, flood_colour)
    win_check()
    
#main code
app = App("Fill The Board!")
board = Waffle(app, width=board_size, height=board_size, pad=0)
palette = Waffle(app, width=6, height=1, dotty=True, command=start_flood)

win_text = Text(app)

fill_board()
init_palette()
app.display()