import gameclass
import random

def damageCalculation(x,y):

    if x == "Hit" and y == "Miss":
        return 1
    if x == "Miss" and y == "Hit":
        return 2
    if x == "Hit" and y == "Hit":
        return 3
    if x == "Defend" and y == "Hit":
        return 4
    if x == "Defend" and y == "Miss":
        return 5
    if x == "Hit" and y == "Defend":
        return 6
    if x == "Miss" and y == "Defend":
        return 7
    if x == "Defend" and y == 'Defend':
        return 8


def main():
    goo = gameclass.Enemy([0,0],2000)
    hero = gameclass.Hero([0,0],2,40,2,100,3)
    goo.enemyName("Goo")





    hero.heroName(input("Hey there hero! What's your name? "))
    print("Fight the "+goo.Name+", "+ hero.Name)
    while 1:
        valid = True
        if hero.HP <= 0:
            hero.Die()
            break
        if goo.HP <= 0:
            goo.Die()
            break
        action = (input("What would you like to do? 1) Defend 2) Attack:  "))
        if action == "1":
            heroaction = hero.Defend()
        if action == "2":
            heroaction = hero.Attack()
        if action != "1" and action != "2":
            print("Please enter a valid choice")
            valid = False
        if valid:
            enemychoice = random.choice([1,2])
            if enemychoice == 1:
                enemyaction = goo.Attack()
            if enemychoice == 2:
                enemyaction = goo.Defend()
            results = damageCalculation(heroaction,enemyaction)
        if valid == False:
            continue
        if results == 1:
            goo.HP -= 25
        if results == 2:
            hero.HP -= 25
        if results == 3:
            hero.HP -= 10
            goo.HP -= 10
        if results == 4:
            hero.HP -= 10
        if results == 5:
            valid = True
        if results == 6:
            goo.HP -= 10
        if results == 7:
            valid = True
        if results == 8:
            valid = True
        print(hero.Name+ "'s HP is "+str(hero.HP))
        print(goo.Name+"'s HP is "+str(goo.HP))
    print("The end!")
main()
