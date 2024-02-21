liste_distance_villes = [[0,253,360,669,959,868], #distance Asti et autre
                         [253,0,110,471,725,729], #distance Bologne et autre
                         [360,110,0,383,617,663], #distance Rimini et autre
                         [669,471,383,0,335,312], #distance Napoli et autre
                         [959,725,617,335,0,483], #distance Lecce et autre
                         [868,729,663,312,493,0]] #distance Palermo et autre

villes = ["Asti", "Bologne", "Rimini", "Napoli", "Lecce", "Palermo"]

def probleme_voyageur(distances: list, noms_villes: list, depart: int):
    listeOrdreVilles = []
    villeAvant = depart
    distance = 0
    condition = [False,False,False,False,False,False] #passer par toute les villes
    for i in range(len(villes)):
        listeOrdreVilles.append(villes[villeAvant])
        condition[villeAvant] = True

        minimum = liste_distance_villes[villeAvant][0]
        for element in liste_distance_villes[villeAvant]:
            if element < minimum and element != 0 and condition[liste_distance_villes[villeAvant].index(element)] == False:
                minimum = element

        villeActuel = liste_distance_villes[villeAvant].index(minimum)

        distance += liste_distance_villes[villeAvant][villeActuel]
        condition[villeActuel] = True
        villeAvant = villeActuel
    return distance,listeOrdreVilles

print(probleme_voyageur(liste_distance_villes, villes, 3))
