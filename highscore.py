def check_high_score(wave):
    try:
        high = int(open("highscore.txt", "r").read())
        if wave > high:
            writeIt = open("highscore.txt","w")
            writeIt.write(str(wave))
            return wave
        else:
            return high
    except FileNotFoundError:
        score = open("highscore.txt", "w")
        score.write(str(wave))
def reset_high_score():
    score = open("highscore.txt","w")
    score.write("0")
