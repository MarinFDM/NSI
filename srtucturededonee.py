todo_liste = { "faire les courses" : True, "ranger le garage" : False, "completer l exercice 4" : False}

def tacheàfaire():
    taille = 0
    for t in todo_liste.keys():
        if not todo_liste[t]:
            taille += 1
    return taille
            
def addtask(cle,valeur): #addtask
    todo_liste[cle] = valeur

def deltask(cle):
    del todo_liste[cle]

def modtask(cle): #change statut task
    todo_liste[cle] = not todo_liste[cle]

def listtacheàfaire():
    for t in todo_liste.keys():
        if not todo_liste[t]:
            print(t,todo_liste[t])

def interface():
    stop = True
    while stop:
        liste = list(todo_liste.keys())
        for i in range(0,len(liste)):
            print(i,liste[i],todo_liste[liste[i]])   
        a = input("quelle action veut tu faire(+/-/v/?/x)")
        match a:
            case '+':
                cle = input("quelle est le nom de tache de la tache ? ")
                addtask(cle,False)
            case '?':
                listtacheàfaire()
            case '-':
                num = int(input("quelle est le numero de la tache a supprimer ?"))
                for i in range(0,len(liste)):
                    if num == i:
                        deltask(liste[i])
            case 'v':
                num2 = int(input("quelle tache veut tu modifier?"))
                for i in range(0,len(liste)):
                    if num2 == i:
                        modtask(liste[i])   
            case 'x':
                stop = False
interface()


# print(todo_liste.keys())
# print(todo_liste.values())
# keyList = list(todo_liste.keys())
# print(keyList[1])

# for i in range(0,len(keys)):
#     print(i+1,keys[i],todo_liste[keys[i]])
# print('++++++++')
# count = 0
# for key,value in todo_liste.items():
#     count += 1
#     print(count,key,value)
# print('++++++++')
# for id,key in enumerate(todo_liste.keys()):
#     print(id+1,key,todo_liste[key])


# def chelou(numero):
#     return numero-1,numero+1

# print(chelou(5))
# print(enumerate(todo_liste.keys()))


# for t in todo_liste.keys():
#          print(t,todo_liste[t])
# print("----------------------")
# deltask("faire les courses")
# for t in todo_liste.keys():
#          print(t,todo_liste[t])


# print(todo_liste["faire les courses"])
# v("faire les courses")
# print(todo_liste["faire les courses"])
# v("faire les courses")
# print(todo_liste["faire les courses"])
