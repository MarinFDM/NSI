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
