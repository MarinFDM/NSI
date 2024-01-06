import random
def carte_valide(carte):
    result = False
    numero , signe = carte
    valeurs = ['2','3','4','5','6','7','8','9','10','11','12','13','14']
    couleurs = ['Pique', 'Coeur', 'Carreau', 'Trefle']
    for valeur in valeurs:
        if valeur == numero:
            result = True
            break
        else:
            result = False
    if not result:
        return result
    for couleur in couleurs:
        if couleur == signe:
            result = True
            break
        else:
            result = False
    return result

def nom_carte(carte):
    dict = {11 : 'valet' , 12: 'Dame' , 13: 'Roi', 14: 'As'}
    numero, signe = carte
    if numero > 10:
        val = dict[numero]
    else:
        val = str(numero)
    return val + " de " + signe 

def jeudecarte():
    valeurs = ['2','3','4','5','6','7','8','9','10','11','12','13','14']
    couleurs = ['Pique', 'Coeur', 'Carreau', 'Trefle']
    Liste=[]
    for i in range(len(valeurs)):
        for t in range(len(couleurs)):
            Liste.append((int(valeurs[i]),couleurs[t]))
    return Liste

def tire_une_carte(jeu):
    num = random.randint(0,51)
    return jeu[num]

jeu = jeudecarte()
for i in range(5):
    print(nom_carte(tire_une_carte(jeu)))




# jeu=jeudecarte()
#     for carte in jeu:
#         print(nom_carte(carte))

