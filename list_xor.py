#list_xor(1, [1, 2, 3], [4, 5, 6]) == True
#list_xor(1, [0, 2, 3], [1, 5, 6]) == True
#list_xor(1, [1, 2, 3], [1, 5, 6]) == False
#list_xor(1, [0, 0, 0], [4, 5, 6]) == False

def list_xor(number, list1, list2):
    bandera_1 = 0
    bandera_2 = 0

    if number in list1:
        bandera_1 = 1
    
    if number in list2:
        bandera_2 = 1

    return bandera_1 ^ bandera_2

print(list_xor(1, [1, 2, 3], [4, 5, 6]))
print(list_xor(1, [0, 2, 3], [1, 5, 6]))
print(list_xor(1, [1, 2, 3], [1, 5, 6]))
print(list_xor(1, [0, 0, 0], [4, 5, 6]))
