def tri(list):
    for i in range(len(list)):
        val = list[i]
        pos = i
        while pos>0 and list[pos-1] < val:
            list[pos] = list[pos-1]
            pos-=1
        list[pos] = val
    return list

def tri_bulle(liste):
    n = len(liste)
    for i in range(n-1):
        for j in range(n-i-1):
            print(liste,i,j )
            if liste[j] >liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
                print(liste,i,j )
    return liste

def minimum(Liste):
    minimum = Liste[0]
    for element in Liste:
        if element < minimum:
            minimum = element
    return Liste.index(minimum)


def tri_sellection(Liste):
    valeurachanger=0
    a=0
    b=len(Liste)
    for i in range(len(Liste[a:b])):
        idmini = minimum(Liste[a:b])+a
        valeurachanger = Liste[a]
        if Liste[a] != Liste[idmini]:
            Liste[a] , Liste[idmini] = Liste[idmini] , Liste[a]
        a+=1
    return Liste
print(tri_sellection([9, 5, 8, 6, 4,-2, 15, 88, -25, 80, 33, 60, 2, 5, 505]))


def maximum(Liste):
    maximum = Liste[0]
    for element in Liste:
        if element > maximum:
            maximum = element
    return Liste.index(maximum)

def tri_sellectionparlafin(Liste):
    a=0
    b=len(Liste)
    for i in range(len(Liste[a:b])):
        idmax = maximum(Liste[a:b])+b
        if Liste[b] != Liste[idmax]:
            Liste[b] , Liste[idmax] = Liste[idmax] , Liste[b]
        b-=1
    return Liste
print(tri_sellectionparlafin([9, 5, 8, 6, 4,-2, 15, 88, -25, 80, 33, 60, 2, 5, 505]))

from math import*
# def est_present_dans(tableau_trié, valeur):
#     while len(tableau_trié) != 1:
#         a = len(tableau_trié)//2
#         if valeur <= tableau_trié[a]:
#             tableau_trié = tableau_trié[0:a]
#         else :
#             tableau_trié = tableau_trié[a+1:len(tableau_trié)]
#     if valeur == tableau_trié[0]:
#         result = True
#     else:
#         result = False
#     return result , tableau_trié

# print(est_present_dans([2,3,5,5,6,7],1))

def fctn(x):
    result = cos(x)-x
    return result

def rech_fct_dicho(a:int,b:int,p):
    mid = 0.0
    while b-a>10**-p:
        mid = (a+b)/2
        if fctn(mid) > 0.0:
            a = mid
        else:
            b = mid
    mid = round(mid,4)
    return mid
print(rech_fct_dicho(0,4,4))
