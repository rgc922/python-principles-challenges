def convert(lista):
    
    #for x in range(len(lista)): lista[x] = str(lista[x])
    #return lista
    return [str(x) for x in (lista)]

print(convert([1, 2, 3]))
