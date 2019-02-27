import random
character_names = []

# reads the names from the text file
with open('Character-names.txt', 'r') as filehandle:  
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]

        # add item to the list
        character_names.append(currentPlace)

# displays into message
def intro_message():
    print("_____________")
    print("|            |")
    print("|   Smash    |")
    print("|    Bros.   |")
    print("|    Top     |")
    print("|    Trumps  |")    
    print("|____________|")
    print("(\__/) ||")
    print("(•ㅅ•) ||")
    print("/ 　 づ")
    print("")

# cards directory 

character_cards = []

def create_cards():
    character_cards.append([character_names[0],random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)])
    character_cards.append([character_names[1],random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)])   
    character_cards.append([character_names[2],random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)])
    character_cards.append([character_names[3],random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)])
    character_cards.append([character_names[4],random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)])
    character_cards.append([character_names[5],random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)])
    character_cards.append([character_names[6],random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)])
    character_cards.append([character_names[7],random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)])
    character_cards.append([character_names[8],random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)])
    character_cards.append([character_names[9],random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)])
    character_cards.append([character_names[10],random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)])
    character_cards.append([character_names[11],random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)])
    character_cards.append([character_names[12],random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)])
    character_cards.append([character_names[13],random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)])
    character_cards.append([character_names[14],random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)])

# generates random card for user
def draw_card():
    print("Your Card:")
    cardNumber = random.randint(0,len(character_cards)-1)
    print("---> Name: " + character_cards[cardNumber][0])
    print("---> Power: " + str(character_cards[cardNumber][1]))
    print("---> Agility: " + str(character_cards[cardNumber][2]))
    print("---> Grab & Throw: " + str(character_cards[cardNumber][3]))
    print("---> Taunt: " + str(character_cards[cardNumber][4]))    

# main function
def main():
    intro_message()
    create_cards()
    draw_card()   

main()