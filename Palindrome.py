def palindrome(Str_get):
    
    list_test = []
    str_test = ""

    for x in range(len(Str_get)):
        print(x)
        list_test.append(Str_get[x])
    list_test.reverse()
    #print(list_test)

    for x in range(len(list_test)):
        str_test += list_test[x]
    print(str_test)

    if str_test == Str_get:
        return True
    else:
        return False

print(palindrome("anilina"))
