## score = ABS(20 - temp) + speed + ABS(220 - direction) x 0.1

def getScore(t,s,d):
  score = abs(20 - t) + s + abs(220 - d) * 0.1
  return score
