def format_number(number):

    number = str(number)
    list_number = []
    list_final = []
    str_return = ''
    
    for x in range(len(number)):
        #print("counter ", counter, counter % 3)
        list_number.insert(x, number[x])
        #list_number.append(x)
    #print(list_number)    
    list_number.reverse()

    counter = 0
    for x in range(len(list_number)):
        counter += 1
        list_final.append(list_number[x])
        if counter % 3 == 0:
            list_final.append(',')

    list_final.reverse()

    if list_final[0] == ',':
        del list_final[0]

    for x in list_final:
        str_return += x

    return str_return

print(format_number(1000000))
print(format_number(100000))
print(format_number(123456))
