def highScore(wave):
    try:
        high = int(open("highscore.txt", "r").read())
        if wave> high:
            writeIt = open("highscore.txt","w")
            writeIt.write(str(wave))

    except FileNotFoundError:
        score = open("highscore.txt", "w")
        score.write(str(wave))
