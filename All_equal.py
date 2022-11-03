def all_equal(lista):
    #print(lista)
    for x in (lista):
        #print(x)
        for y in (lista):
            #print(x, y)
            if x != y:
                return False
   
            
    return True
    

print(all_equal([1, 1, 1]))
