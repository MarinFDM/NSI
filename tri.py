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

def tri_sellection(Liste):
    trie1 = 0
    trie2=0
    a=0
    b=len(Liste)
    Liste=[]
    for i in range(len(Liste[a, b])):
        if Liste[i] < Liste[i+1]:
            trie1 = Liste[i]
        trie1, trie2 = Liste[a], Liste[i]

