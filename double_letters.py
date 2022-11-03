def double_letters(str_check):
    
    bandera = False
    for x in range(len(str_check)):
        #print(x)
        if x == 0:
            continue
        if str_check[x] == str_check[x - 1]: 
            bandera = True
    
    return bandera


print(double_letters("nono"))
