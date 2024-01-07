from math import *
def ex1(mdp:str):
    result = False
    trouveUneMinuscule = False 
    trouveUneMajuscule  = False
    trouverUnNombre = False 
    trouveUnSpecial = False
    if len(mdp) < 8:
        return False
    for c in mdp:
        if c.islower():
            trouveUneMinuscule = True
        if c.isupper():
            trouveUneMajuscule = True
        if c.isdigit():
            trouverUnNombre = True
        if not (c.isalpha() or c.isdigit() or c.isspace()):
            trouveUnSpecial = True
    return trouveUneMinuscule and trouveUneMajuscule and trouverUnNombre and trouveUnSpecial

# print(ex1('aA#7'))
# print(ex1('aA#7ppppp'))
# print(ex1('123456789'))

def ex2(mot):
    List = mot.split(' ')
    return len(List)
# print(ex2("Marin est au ski"))
# print(ex2("Python"))

def ex4(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    x3 = (x1+x2)/2
    y3 = (y1+y2)/2
    return ((int(x3),int(y3)))
# print(ex4((2,2),(4,4)))

def ex5(p1,p2):
    result = sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2) 
    return result

# print(ex5((2,2),(4,4)))
