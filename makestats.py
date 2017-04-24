import mobclass

def makeHealth(wave):
	healthbase = 9
	health = healthbase + (float(wave))**1.20
	return health
def makeStrength(wave):
	strbase = 0
	strength = strbase + wave**1.15
	return strength
