def tri(list):
    for i in range(len(list)):
        val = list[i]
        pos = i
        while pos>0 and list[pos-1] > val:
            list[pos] = list[pos-1]
            pos-=1
        list[pos] = val
    return list

print(tri([1,3,5,76,877,456,34,23,56,0]))
