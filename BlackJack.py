# BLACCKJACK PROJECT
import random
def pick_card():
    "Returns a random card from the deck"
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if(sum(cards)==21 and len(cards)==2):
        return 0      #So, when score is 21 and we have only 2 cards, 0 will represent a blackjack in our game
    if(11 in cards and sum(cards)>21):

        cards.remove(11)
        cards.append(1)
    return sum(cards)

def computer_play(cards):
    "This is how computer picks the cards and play"
    if(sum(cards)>=17):
        return cards
    cards.append(pick_card())
    return computer_play(cards)

logo = '''
.------.            _     _            _    _            _    
|A_  _ |           | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
      |  \/ K|                            _/ |                
      '------'                           |__/  
       '''
to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")          #To start the game
print('\n'*15)
print(logo)
while(to_play=='y'):
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(pick_card()) 
        computer_cards.append(pick_card())
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"    Your cards: {user_cards}, current score: {user_score}")
    print(f"    Computer's first card: {computer_cards[0]}")

    "Here, we check if user or computer has blackjack or user went over 21 and if any condition hits we end the game."

    if(user_score==0 or computer_score==0 or user_score>21):
        to_play='n'
        if(user_score==0):
            print("You win with a BlackJack 😁")
        elif(computer_score==0):
            print("Lose, opponenet has BlackJack 😞")
        elif(user_score>21):
            print("You went over. You lose 😞")
    else:
        user_play = input("Type 'y' to get aother card, type 'n' to pass: ")

        "This loop is for the user to continue his game by picking another card or end it."

        while(user_play=='y'):
            user_cards.append(pick_card())
            user_score = calculate_score(user_cards)
            print(f"    Your cards: {user_cards}, current score: {user_score}")
            print(f"    Computer's first card: {computer_cards[0]}")
            if(user_score>21):
                user_play = 'n'
                print(f"    Your final hand: {user_cards}, final score: {user_score}")
                print(f"    Computer's final hand: {computer_cards[0]}, final score: {computer_cards[0]}")
                print("You went over. You lose 😞")
                break
            user_play = input("Type 'y' to get aother card, type 'n' to pass: ")
        
        "So, user has passed the game and now computer will pick cards until it wants and final scor is shown."

        if(user_score<=21):
            computer_cards = computer_play(computer_cards)
            computer_score = calculate_score(computer_cards)
            print(f"    Your final hand: {user_cards}, final score: {user_score}")
            print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
            if(user_score>computer_score):
                print("You win 😁")
            elif(user_score==computer_score):
                print("Draw 😐")
            elif(user_score<computer_score):
                if(computer_score>21):
                    print("Opponent went over. You win 😁")
                else:
                    print("You lose 😞")
    to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
