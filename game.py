import os
import time 
import random 
from Square import Square 
class Board(object):
        
	def make_monster(self):
		y=random.randint(0,self.height-1)
		x=random.randint(0, self.width-1)
		if (self.squares[x,y].monster==True or (x==self.treasure_x and y==self.treasure_y)):
			self.make_monster()
		else:
			self.squares[x,y].monster=True

			
	def __init__(self, width , height , number_of_monsters ):
		self.width =width 
		self.height =height 
		self.number_of_monsters=number_of_monsters 
		self.game_over=False 
		self.treasure_x=random.randint(0,width - 1 )
		self.treasure_y =random.randint(0,height-1)
		self.squares={}
		for i in range (height):
			for j in range (width):
				self.squares[(j,i)]=Square(j, i, self.treasure_x, self.treasure_y)
		self.previous_distance=float('inf')
		for m in range (min(number_of_monsters, width*height-1)):
			self.make_monster()
			
	def guess_square(self, x, y):
		if (x==self.treasure_x and y==self.treasure_y):
			print("you guessed right")
			os.system("say 'you guessed right'")
			self.game_over=True
		elif (self.squares[x,y].monster==True):
			print("you lose")
			os.system("say 'you lose'")
			self.game_over=True
		else:
			print("go on")
			os.system("say 'go on'")
			if (self.squares[x,y].distance_to_treasure<self.previous_distance):
				print("you are getting closer")
				os.system("say 'you are getting closer'")
			elif (self.squares[x,y].distance_to_treasure>self.previous_distance):
				print("you are getting farther")
				os.system("say 'you are getting farther'")
			self.previous_distance=self.squares[x,y].distance_to_treasure
		
