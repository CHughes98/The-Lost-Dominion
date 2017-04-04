import random
import math

class Enemy:


	def __init__(self,position,HP):
		self.Name = ''
		self.Image = ''
		self.Position = position
		self.Alive = True
		self.HP = HP
		print("The enemy was initialized")

	def enemyName(self,name):
		self.Name = name
		print(self.Name)
		print("The enemy is now named")
	def Sprite(self,image):
		self.Sprite = image
		print(self.Sprite)
		print("The enemy's sprite is loaded")

	def moveHorizontal(self,distancex):
		if self.Alive:
			self.Position[0]+= distancex
			print(self.Position)
			if distancex <0:
				print("The enemy moved left "+str(abs(distancex)))
			if distancex >0:
				print("The enemy moved right "+str(abs(distancex)))
			if distancex == 0:
				print("The enemy did not move.")
		if not self.Alive:
			print("The enemy is dead and cannot move")

	def moveVertical(self, distancey):
		if self.Alive:
			self.Position[1]+= distancey
			print(self.Position)
			if distancey <0:
				print("The enemy moved down "+str(abs(distancey)))
			if distancey >0:
				print("The enemy moved up "+str(abs(distancey)))
			if distancey == 0:
				print("The enemy did not move.")
		if not self.Alive:
			print("The enemy is dead and cannot move")

	def Attack(self):
		if self.Alive:
			self.hit = random.choice([0,1])
			if self.hit == 0:
				print("The enemy missed")
				return "Miss"
			if self.hit == 1:
				print("The enemy hit")
				return "Hit"
		if not self.Alive:
			print("The enemy is dead and cannot attack")

	def Defend(self):
		print("The enemy raised its defenses")
		return "Defend"

	def Die(self):
		self.Alive = False
		print("The enemy died")


class Hero:


	def __init__(self,position,HP,skillPoints,stren,spd,smarts):
		self.Name = ''
		self.Image = ''
		self.Position = position
		self.Alive = True
		self.HP = HP
		self.skillPoints = skillPoints
		self.stren = stren
		self.spd = spd
		self.smarts = smarts
		print("The Hero was initialized")

	def heroName(self,name):
		self.Name = name
		print(self.Name)
		print("The Hero is now named")

	def setstats(self):
		for x in range(11):
			pie = input("Choose a stat to increase. You have "+ str(10-x)+ " Skill points left: 1) Strength 2) Speed 3) Intelligence: ")

	def checkstats(self):
		if self.stren+self.spd+self.smarts > 10:
			print("You can't do math, so I'm picking your stats.")
			self.stren = 4
			self.spd = 3
			self.smarts = 3

	def Sprite(self,image):
		self.Sprite = image
		print(self.Sprite)
		print("The Hero's sprite is loaded")

	def moveHorizontal(self,distancex):
		if self.Alive:
			self.Position[0]+= distancex
			print(self.Position)
			if distancex <0:
				print("The Hero moved left "+str(abs(distancex)))
			if distancex >0:
				print("The Hero moved right "+str(abs(distancex)))
			if distancex == 0:
				print("The Hero did not move.")
		if not self.Alive:
			print("The Hero is defeated and cannot move")

	def moveVertical(self, distancey):
		if self.Alive:
			self.Position[1]+= distancey
			print(self.Position)
			if distancey <0:
				print("The Hero moved down "+str(abs(distancey)))
			if distancey >0:
				print("The Hero moved up "+str(abs(distancey)))
			if distancey == 0:
				print("The Hero did not move.")
		if not self.Alive:
			print("The Hero is defeated and cannot move")

	def Attack(self):
		if self.Alive:
			self.hit = random.choice([0,1])
			if self.hit == 0:
				print("The Hero missed")
				return "Miss"
			if self.hit == 1:
				print("The Hero hit")
				return "Hit"

		if not self.Alive:
			print("The Hero is defeated and cannot attack")
	def Defend(self):
		print("The hero raised their defenses")
		return "Defend"
	def Die(self):
		self.Alive = False
		print("The Hero was defeated")
