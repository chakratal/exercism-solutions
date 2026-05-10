import math

def score(x, y):
    points = 0
    
    if math.sqrt(x**2 + y**2) > 10:
        points += 0
    if 5 < math.sqrt(x**2 + y**2) <=10:
        points += 1
    if 1 < math.sqrt(x**2 + y**2) <=5: 
        points += 5
    if math.sqrt(x**2 + y**2) <=1: 
        points += 10
    return points
