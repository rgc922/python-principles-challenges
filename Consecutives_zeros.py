def consecutive_zeros(Str_number):
    counter = 0
    general_counter = 0
    for x in Str_number:
        #print(x)
        if x == "0":
            counter += 1
            if general_counter <= counter:
                general_counter = counter
        else:
            
            counter = 0
    return general_counter

print(consecutive_zeros("1001101000110"))
#print(consecutive_zeros("0"))
