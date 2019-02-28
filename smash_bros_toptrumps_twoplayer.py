import random # gets random directory
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
    print("()___/) ||")
    print("( •ㅅ•) ||")
    print("/ 　 づ")
    print("")

# cards directory 
def create_cards():
    global player_1_cards
    global player_2_cards

    player_1_cards = []
    player_2_cards = []

    for i in range(8):
        player_1_cards.append([character_names[random.randint(0,15)],random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)])
    
        player_2_cards.append([character_names[random.randint(0,15)],random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)])

def draw_player_1():
    global p1_power
    global p1_agility
    global p1_grab
    global p1_taunt
    cardNumber = random.randint(0,len(player_1_cards)-1)

    name = player_1_cards[cardNumber][0]
    p1_power = player_1_cards[cardNumber][1]
    p1_agility = player_1_cards[cardNumber][2]
    p1_grab = player_1_cards[cardNumber][3]
    p1_taunt = player_1_cards[cardNumber][4]

    print("Here is Player 1's card:")
    print("........................")
    print("---> Name: " + name)
    print("---> Power: " + str(p1_power))
    print("---> Agility: " + str(p1_agility))
    print("---> Grab & Throw: " + str(p1_grab))
    print("---> Taunt: " + str(p1_taunt))
    print("........................")
    print(" ")

def draw_player_2():
    global p2_power
    global p2_agility
    global p2_grab
    global p2_taunt
    cardNumber = random.randint(0,len(player_2_cards)-1)

    name = player_2_cards[cardNumber][0]
    p2_power = player_2_cards[cardNumber][1]
    p2_agility = player_2_cards[cardNumber][2]
    p2_grab = player_2_cards[cardNumber][3]
    p2_taunt = player_2_cards[cardNumber][4]


    print("Here is Player 2's card:")
    print("........................")
    print("---> Name: " + name)
    print("---> Power: " + str(p2_power))
    print("---> Agility: " + str(p2_agility))
    print("---> Grab & Throw: " + str(p2_grab))
    print("---> Taunt: " + str(p2_taunt))
    print("........................")



# the main game function
def game(): 
    create_cards()

    p1_card_count = 8
    p2_card_count = 8

    while p1_card_count or p2_card_count > 0:

        print(" ")
        print(".................")
        print(">>> New Round <<<")
        print(".................")
        print(" ")
        print("Player 1's Turn")
        print(" ")
        draw_player_1()
        draw_player_2()

        turn_1 = input("What attribute would you like to call out, Player One?")
        if turn_1 == "power":
            if p1_power > p2_power:
                print("Player 1 wins.")
                p1_card_count += 1
                p2_card_count -= 1
                print("Player 1 now has " + str(p1_card_count) + " cards")
                print("Player 2 now has " + str(p2_card_count) + " cards")
                
            elif p1_power < p2_power:
                print("Player 2 wins.")
                p1_card_count -= 1
                p2_card_count += 1
                print("Player 1 now has " + str(p1_card_count) + " cards")
                print("Player 2 now has " + str(p2_card_count) + " cards")
                

        elif turn_1 == "agility":
            if p1_agility > p2_agility:
                print("Player 1 wins.")
                p1_card_count += 1
                p2_card_count -= 1
                print("Player 1 now has " + str(p1_card_count) + " cards")
                print("Player 2 now has " + str(p2_card_count) + " cards")
                
            elif p1_agility < p2_agility:
                print("Player 2 wins.")
                p1_card_count -= 1
                p2_card_count += 1
                print("Player 1 now has " + str(p1_card_count) + " cards")
                print("Player 2 now has " + str(p2_card_count) + " cards")
                

        elif turn_1 == "taunt":
            if p1_taunt > p2_taunt:
                print("Player 1 wins.")
                p1_card_count += 1
                p2_card_count -= 1
                print("Player 1 now has " + str(p1_card_count) + " cards")
                print("Player 2 now has " + str(p2_card_count) + " cards")
                
            elif p1_taunt < p2_taunt:
                print("Player 2 wins.")
                p1_card_count -= 1
                p2_card_count += 1
                print("Player 1 now has " + str(p1_card_count) + " cards")
                print("Player 2 now has " + str(p2_card_count) + " cards")
                
        
        elif turn_1 == "grab":
            if p1_grab > p2_grab:
                print("Player 1 wins.")
                p1_card_count += 1
                p2_card_count -= 1
                print("Player 1 now has " + str(p1_card_count) + " cards")
                print("Player 2 now has " + str(p2_card_count) + " cards")
                
            elif p1_grab < p2_grab:
                print("Player 2 wins.")
                p1_card_count -= 1
                p2_card_count += 1
                print("Player 1 now has " + str(p1_card_count) + " cards")
                print("Player 2 now has " + str(p2_card_count) + " cards")
                
        else:
            print("I didn't understand that.")

        print(" ")
        print("Player 2's Turn")
        print(" ")
        draw_player_1()
        draw_player_2()

        turn_2 = input("What attribute would you like to call out, Player Two?")
        if turn_2 == "power":
            if p1_power > p2_power:
                print("Player 1 wins.")
                p1_card_count += 1
                p2_card_count -= 1
                print("Player 1 now has " + str(p1_card_count) + " cards")
                print("Player 2 now has " + str(p2_card_count) + " cards")
                
            elif p1_power < p2_power:
                print("Player 2 wins.")
                p1_card_count -= 1
                p2_card_count += 1
                print("Player 1 now has " + str(p1_card_count) + " cards")
                print("Player 2 now has " + str(p2_card_count) + " cards")
                

        elif turn_2 == "agility":
            if p1_agility > p2_agility:
                print("Player 1 wins.")
                p1_card_count += 1
                p2_card_count -= 1
                print("Player 1 now has " + str(p1_card_count) + " cards")
                print("Player 2 now has " + str(p2_card_count) + " cards")
                
            elif p1_agility < p2_agility:
                print("Player 2 wins.")
                p1_card_count -= 1
                p2_card_count += 1
                print("Player 1 now has " + str(p1_card_count) + " cards")
                print("Player 2 now has " + str(p2_card_count) + " cards")
                

        elif turn_2 == "taunt":
            if p1_taunt > p2_taunt:
                print("Player 1 wins.")
                p1_card_count += 1
                p2_card_count -= 1
                print("Player 1 now has " + str(p1_card_count) + " cards")
                print("Player 2 now has " + str(p2_card_count) + " cards")
                
            elif p1_taunt < p2_taunt:
                print("Player 2 wins.")
                p1_card_count -= 1
                p2_card_count += 1
                print("Player 1 now has " + str(p1_card_count) + " cards")
                print("Player 2 now has " + str(p2_card_count) + " cards")
                
        
        elif turn_2 == "grab":
            if p1_grab > p2_grab:
                print("Player 1 wins.")
                p1_card_count += 1
                p2_card_count -= 1
                print("Player 1 now has " + str(p1_card_count) + " cards")
                print("Player 2 now has " + str(p2_card_count) + " cards")
                
            elif p1_grab < p2_grab:
                print("Player 2 wins.")
                p1_card_count -= 1
                p2_card_count += 1
                print("Player 1 now has " + str(p1_card_count) + " cards")
                print("Player 2 now has " + str(p2_card_count) + " cards")
                        
        else:
            print("I didn't understand that.")

        if p1_card_count == 0:
            print("Congratulations, Player 2 wins.")
            exit()
            
        elif p2_card_count == 0:
            print("Congratulations, Player 1 wins.")
            exit()

# main function
def main():
    intro_message()

    start = input("Would you like to start a new game?").lower()
    if start == ("yes"):
        game()
    else:
        print("Sorry, I didn't understand that.")
        exit()
    

# starts the program
main()