def equilateral(sides):
    for i in sides:
        if i > 0:
            return sides[0] == sides[1] and sides[1] == sides[2]
        return False
        
def isosceles(sides):
    for i in sides:
        if i > 0:
            if sides[0] + sides[1] < sides[2] or sides[0] + sides[2] < sides[1] or sides[1] + sides[2] < sides[0]:
                return False
            if sides[0] + sides[1] >= sides[2] or sides[0] + sides[2] >= sides[1] or sides[1] + sides[2] >= sides[0]:
                return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]  
        return False
        
def scalene(sides):
    for i in sides:
        if i > 0:
            if sides[0] + sides[1] < sides[2] or sides[0] + sides[2] < sides[1] or sides[1] + sides[2] < sides[0]:
                return False
            return sides[0] != sides[1] != sides[2] != sides[0]
        return False
