def zap(list1, list2):
    list_return = []

    for x in range(len(list1)):
        list_return.append((list1[x],list2[x]))

    return list_return

print(zap(
    [0, 1, 2, 3],
    [5, 6, 7, 8]
))
