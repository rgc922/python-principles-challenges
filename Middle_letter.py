def mid(Str_check):
    ##print("Funcion ", Str_check)
    if len(Str_check) % 2 == 0:
        return ''
    else:
        return Str_check[(len(Str_check)) // 2]


print(mid("aaaa"))
