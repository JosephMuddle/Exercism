def triangletest(sides):
    return (all([x > 0 for x in sides]) and all([x < (sum(sides) - x) for x in sides]))

def equilateral(sides):
    return ((all([x==sides[0] for x in sides])) and (triangletest(sides)))

def isosceles(sides):
    return (any([(sum([int(x==sides[i]) for x in sides])>=2) for i in range(len(sides))]) and (triangletest(sides)))

def scalene(sides):
    return ((len(set(sides)) == len(sides)) and (triangletest(sides)))
