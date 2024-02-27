from math import sqrt

listeDePoints =[{'attributs': [2,3],'classe':'R'},
                {'attributs': [-1,5],'classe': 'B'},
                {'attributs': [3,3],'classe': 'B'},
                {'attributs': [3,0],'classe': 'R'},
                {'attributs': [6,5],'classe': 'R'},
                {'attributs': [-2,4],'classe': 'R'},
                {'attributs': [-1,-1],'classe': 'B'},
                {'attributs': [0,0],'classe': 'R'},
                {'attributs': [1,1],'classe': 'B'},
                {'attributs': [0,2],'classe':'B'} ]

def distance(occurance,cible):
    xa = occurance["attributs"][0]
    ya = occurance["attributs"][1]
    xb = cible["attributs"][0]
    yb = cible["attributs"][1]
    dist = int(sqrt((xb-xa)**2)+((yb-ya)**2))
    return dist

def LePlusProche(cible,Nbdepoint):
    minimum = listeDePoints[0]
    ListePointLesPlusProche = []
    while len(ListePointLesPlusProche) <= Nbdepoint:

        for i in range(len(listeDePoints)):
            element = listeDePoints[i]
            if distance(minimum,cible) < distance(element,cible):
                minimum = element

        ListePointLesPlusProche.append(minimum['classe'])
        listeDePoints.remove(listeDePoints.index(minimum))

    return ListePointLesPlusProche

def prediction(Nbpoints,cible):
    ListePointLesPlusProche = LePlusProche(cible,Nbpoints)
    for i in range(len(ListePointLesPlusProche)):
        if ListePointLesPlusProche[i] == 'R'
            ListeR.append(ListePointLesPlusProche[i])
        else:
            ListeB.append(ListePointLesPlusProche[i])
    if len(ListeB) > len(<listeR):
        return ListeB
    else:
        return ListeR
            
