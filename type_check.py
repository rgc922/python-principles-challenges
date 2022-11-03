def only_ints(val1, val2):
    print(type(val1))
    if type(val1) == int and type(val2) == int:   
        return True
    else:
        return False

print(only_ints("a", 2))
