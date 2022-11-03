def add_dots(str_check):
    list = []
    str_return = ''
    for item in range(len(str_check)):
        list.append(str_check[item])
    
    for item in range(len(list)):
        if item != len(list) - 1:
            #print(item)
            str_return += list[item] + '.'
        else: 
            str_return += list[item]
    return str_return

def remove_dots(str_check):
    list = []
    str_return = ''
    for item in range(len(str_check)):
        list.append(str_check[item])
    
    for item in range(len(list)):
        if list[item] != '.':
            str_return = str_return + list[item]

    return str_return

print(remove_dots(add_dots("test")))
