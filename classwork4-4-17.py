class character:
	
	def__init__(self, name, speed, strength, intelligence):
		self.name = ''
		self.location = (0,0)
		self.howFast = speed
		self.howStrong = strength
		self.howSmart = intelligence
		if(speed + strength + intelligence > 10):
			print("Something went wrong!")
		elif(speed + strength + intelligence < 10):
			print("Something went wrong!")
		else:
			print("Everything went well!")
	def move(self, horizontal, vertical):
		if(horizontal == 'Left_ArrowKey' or horizontal == 'Right_ArrowKey'):
			self.location(#Add to x)
		elif(vertical == 'Up_ArrowKey' or vertical = 'Down_ArrowKey'):
			self.location(#Add to y)
		
	def fight(self, opponent):
		fightingPoints = self.speed + self.strength + self.intelligence
		if(fightingPoints == 0):
			return opponent
		else:
			self
			
