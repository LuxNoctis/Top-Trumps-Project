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

# the main game function
def game(): 
    
    cpu_card_count = 10
    player_card_count = 10

    def draw_player_card():
        global power
        global agility
        global grab
        global taunt
        cardNumber = random.randint(0,len(character_cards)-1)

        name = character_cards[cardNumber][0]
        power = character_cards[cardNumber][1]
        agility = character_cards[cardNumber][2]
        grab = character_cards[cardNumber][3]
        taunt = character_cards[cardNumber][4]

        print("---> Name: " + name)
        print("---> Power: " + str(power))
        print("---> Agility: " + str(agility))
        print("---> Grab & Throw: " + str(grab))
        print("---> Taunt: " + str(taunt))

    def cpu_draw_card():
        global cpu_power
        global cpu_agility
        global cpu_grab
        global cpu_taunt
        cardNumber = random.randint(0,len(character_cards)-1)
        cpu_power = character_cards[cardNumber][1]
        cpu_agility = character_cards[cardNumber][2]
        cpu_grab = character_cards[cardNumber][3]
        cpu_taunt = character_cards[cardNumber][4]

    while player_card_count or cpu_card_count < 20:

        print("Here is your card.")
        draw_player_card()
        cpu_draw_card()

        turn = input("What attribute would you like to call out?")
        if turn == "power":
            if power > cpu_power:
                print("You win this round.")
                player_card_count += 1
                cpu_card_count -= 1
                print("You now have " + str(player_card_count) + " cards")
                
            elif power < cpu_power:
                print("You lose this round.")
                player_card_count -= 1
                cpu_card_count += 1
                print("You now have " + str(player_card_count) + " cards")
                

        elif turn == "agility":
            if agility > cpu_agility:
                print("You win this round.")
                player_card_count += 1
                cpu_card_count -= 1
                print("You now have " + str(player_card_count) + " cards")
                
            elif agility < cpu_agility:
                print("You lose this round.")
                player_card_count -= 1
                cpu_card_count += 1
                print("You now have " + str(player_card_count) + " cards")
                

        elif turn == "taunt":
            if taunt > cpu_taunt:
                print("You win this round.")
                player_card_count += 1
                cpu_card_count -= 1
                print("You now have " + str(player_card_count) + " cards")
                
            elif taunt < cpu_taunt:
                print("You lose this round.")
                player_card_count -= 1
                cpu_card_count += 1
                print("You now have " + str(player_card_count) + " cards")
                
        
        elif turn == "grab":
            if grab > cpu_grab:
                print("You win this round.")
                player_card_count += 1
                cpu_card_count -= 1
                print("You now have " + str(player_card_count) + " cards")
                
            elif grab < cpu_grab:
                print("You lose this round.")
                player_card_count -= 1
                cpu_card_count += 1
                print("You now have " + str(player_card_count) + " cards")
                
    
        else:
            print("I didn't understand that.")

        if player_card_count == 20:
            break
            print("Congratulations, you win.")
            play_again = input("Would you like to play again?").lower()
            if play_again == "yes":
                game()
            else:
                exit()
    
        elif cpu_card_count == 20:
            break
            print("Unfortunately, you lose.")
            play_again = input("Would you like to play again?").lower()
            if play_again == "yes":
                game()
            else:
                exit()

# main function
def main():
    intro_message()

    start = input("Would you like to start a new game?").lower()
    if start == ("yes"):
        create_cards()
        game()
    else:
        print("Sorry, I didn't understand that.")
        exit()
    
# starts the program
main()
