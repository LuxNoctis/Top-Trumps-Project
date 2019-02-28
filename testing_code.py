import random
character_names = []

# reads the names from the text file
with open('Character-names.txt', 'r') as filehandle:  
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]

        # add item to the list
        character_names.append(currentPlace)

r_number = random.randint(0,10)

cards = {character_names[0]: [r_number, r_number, r_number, r_number], character_names[1]: [r_number, r_number, r_number, r_number], character_names[2]: [r_number, r_number, r_number, r_number], character_names[3]: [r_number, r_number, r_number, r_number], character_names[4]: [r_number, r_number, r_number, r_number], character_names[4]: [r_number, r_number, r_number, r_number], character_names[5]: [r_number, r_number, r_number, r_number], character_names[6]: [r_number, r_number, r_number, r_number], character_names[7]: [r_number, r_number, r_number, r_number], character_names[8]: [r_number, r_number, r_number, r_number], character_names[9]: [r_number, r_number, r_number, r_number], character_names[10]: [r_number, r_number, r_number, r_number], character_names[11]: [r_number, r_number, r_number, r_number], character_names[12]: [r_number, r_number, r_number, r_number], character_names[13]: [r_number, r_number, r_number, r_number], character_names[14]: [r_number, r_number, r_number, r_number], character_names[15]: [r_number, r_number, r_number, r_number]         
player = {name: cards[name] for name in random.sample(cards.keys(), len(cards) // 2)}
computer = {name: cards[name] for name in cards.keys() - player.keys()}
so that:

print(player)
print(computer)