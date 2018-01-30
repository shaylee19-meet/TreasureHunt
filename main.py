import os
from game import Board

def bad_coordinates():
    os.system("say 'bad coordinates'")
    print("bad coordinates")


board=Board(4,5,6)
while (not board.game_over):
    try:
	    os.system("say 'enter x coordinate'")
	    x=int(input("enter x coordinate: "))
	    os.system("say 'enter y coordinate'")
	    y=int(input("enter y coordinate: "))
    except:
	    bad_coordinates()
    if (x>=0 and x<board.width and y>=0 and y<board.height):
    	board.guess_square(x,y)
    else:
    	bad_coordinates()

