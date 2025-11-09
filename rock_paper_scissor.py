# ROCK PAPER SCISSOR GAME PROJECT
import random
rock = '''
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
 
'''                          #we can get these in "ascii.co.uk/art" gy searching in ascii art by "ctrl+f" and search for "finger"
paper = '''
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)

'''
scissor = '''
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
'''
game_images = [rock, paper, scissor]
ran_index = random.randint(0, 2)
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
player = int(input())
if(player>2):
    print("You typed an invalid number. You lose!")
elif(player==ran_index):
    print(game_images[player])
    print("Computer chose:")
    print(game_images[ran_index])
    print("Draw")
elif(player==0 and ran_index==2):
    print(game_images[player])
    print("Computer chose:")
    print(game_images[ran_index])
    print("You win")
elif(ran_index>player):
    print(game_images[player])
    print("Computer chose:")
    print(game_images[ran_index])
    print("You lose")
elif(player>ran_index):
    print(game_images[player])
    print("Computer chose:")
    print(game_images[ran_index])
    print("You win")
