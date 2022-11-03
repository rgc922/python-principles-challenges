statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(dictionary):
    counter = 0
    for element in dictionary:
        #print(dictionary[element])
        if dictionary[element] == 'online':
            counter += 1
    return counter
    

print(online_count(statuses))
