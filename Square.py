class Square(object):
	def __init__(self,x,y, treasure_x, treasure_y):
			self.x=x
			self.y=y
			self.distance_to_treasure=abs(treasure_y-y)+abs(treasure_x-x)
			self.monster =False