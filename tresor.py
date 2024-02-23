from operator import itemgetter
# exemple = [("a",4,2),("b",3,2),("c",8,5)]
# exempleTrie=sorted(exemple,key=itemgetter(1),reverse=True)
# print(exempleTrie)

def tresor():

    tresors = ["b","c","d","e","f","g","h","i","j","k","l","m","n"]
    valeur = [3,8,5,10,7,1,7,3,3,6,12,2,4]
    distance = [2,5,2,7,4,1,4,2,1,4,10,2,1]
    distanceParcouru = 0
    TresorTrouve=[]
    t = []
    rentabilite=[]
    nombreDePoint=0
    compteur = 0

    for i in range(13):
            rentabilite.append((int((valeur[i]/distance[i])*10),tresors[i]))
    rentabiliteTrie=sorted(rentabilite,key=itemgetter(0),reverse=True)

    while distanceParcouru <= 100:
        DernierTresor = rentabiliteTrie[compteur][1]
        compteur += 1

        if distanceParcouru + distance[tresors.index(DernierTresor)] <= 26:
            TresorTrouve.append(DernierTresor)
            nombreDePoint += valeur[tresors.index(DernierTresor)] 
            distanceParcouru += distance[tresors.index(DernierTresor)]
        else:
            return TresorTrouve,nombreDePoint,distanceParcouru
    
print(tresor())