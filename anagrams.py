def is_anagram(str_1, str_2):
    lista1 = []
    for x in str_1:
        lista1.append(x)
    lista1.sort()
    #print(lista1)

    lista2 = []
    for x in str_2:
        lista2.append(x)
    lista2.sort()
    #print(lista2)

    if lista1 == lista2:
        return True
    else:
        return False

print(is_anagram("typhoon", "opython"))
