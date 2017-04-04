import gameclass

def main():


	goo = gameclass.Enemy([100,40],200)
	goo.enemyName("Goo")
	goo.Sprite("goo.png")
	goo.moveHorizontal(50)
	goo.moveHorizontal(-50)
	goo.moveHorizontal(0)
	goo.moveVertical(50)
	goo.moveVertical(-50)
	goo.moveVertical(0)
	for x in range(15):
		goo.Attack()
	goo.Die()
	goo.moveHorizontal(0)
	goo.moveVertical(0)
	goo.Attack()
	John = gameclass.Hero([20,30],100,4,10,10,10)
	John.heroName("John")
	John.Sprite("John.png")
	John.moveHorizontal(50)
	John.moveHorizontal(-50)
	John.moveHorizontal(0)
	John.moveVertical(50)
	John.moveVertical(-50)
	John.moveVertical(0)
	for x in range(15):
		John.Attack()
	John.Die()
	John.moveHorizontal(0)
	John.moveVertical(0)
	John.Attack()


main()
