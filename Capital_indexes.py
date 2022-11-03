def capital_indexes(str_check):
    list_return = []

    for x in range(len(str_check)):
        if str_check[x].isupper():
            list_return.append(x)

    return list_return

print(capital_indexes("HeLlO"))
