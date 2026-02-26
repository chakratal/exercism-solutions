"""Function to determine if a triangle is equilateral, isosceles, or scalene."""

def equilateral(sides):
    for side in sides:
        if side > 0:
            return sides[0] == sides[1] and sides[1] == sides[2]
        return False
        
def isosceles(sides):
    for side in sides:
        if side > 0 and sides[0] + sides[1] < sides[2] or sides[0] + sides[2] < sides[1] or sides[1] + sides[2] < sides[0]:
            return False
        if sides[0] + sides[1] >= sides[2] or sides[0] + sides[2] >= sides[1] or sides[1] + sides[2] >= sides[0]:
            return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]  
        
def scalene(sides):
    for side in sides:
        if side > 0 and sides[0] + sides[1] < sides[2] or sides[0] + sides[2] < sides[1] or sides[1] + sides[2] < sides[0]:
            return False
        return sides[0] != sides[1] != sides[2] != sides[0]