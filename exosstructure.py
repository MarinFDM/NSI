from math import sqrt
def ex1(mdp:str):
    result = False
    if len(mdp) >= 8:
        result = True
    else:
        return False
    if mdp.islower():
        result = True
    else:
        return False
    if mdp.isupper():
        result = True
    else:
        return False
    if mdp.isdigit():
        result = True
    else:
        return False
    if not (mdp.isalpha() or mdp.isdigit() or mdp.isspace()):
        result= True
    else:
        return False
    return result

def ex2(mot):
    List = mot.split(' ')
    return len(List)

def ex4(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    x3 = (x1+x2)/2
    y3 = (y1+y2)/2
    return ((x3,y3))


def ex5(p1,p2):
    result = sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2) 
    return result
