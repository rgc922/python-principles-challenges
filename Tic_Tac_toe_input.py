def get_row_col(Str_get):

    letter = Str_get[0]
    number = int(Str_get[1]) - 1

    if letter == 'A':
        letter_num = 0
    elif letter == 'B':
        letter_num = 1
    elif letter == 'C':
        letter_num = 2
    
    #print(letter_num, number)
    return (number, letter_num)

print(get_row_col("A3"))
