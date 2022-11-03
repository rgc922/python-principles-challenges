def flatten(listas):
    list_return = []

    #print(len(listas[1]))

    for x in range(len(listas)):
        for y in range(len(listas[x])):
            list_return.append(listas[x][y])
    

    return list_return

print(flatten([[1, 2], [3, 4]]))
