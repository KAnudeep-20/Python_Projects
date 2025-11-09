#HANGMAN GAME
import random
from ASCII_art import stages, logo
from Project_Data import word_list
w1 = random.choice(word_list).upper()
placeholder = "_" * len(w1)
print(logo)
gameover = False
k = 0
while(not gameover):
    if(k==6):
        print("****************YOU LOSE****************")
        print(stages[6])
        print(f"The correct word is {w1}")
        gameover = True
        continue
    if "_" not in placeholder:
        print(w1)
        print("****************YOU WIN****************")
        break
    print(placeholder)
    print(stages[k])
    l = input("Guess a letter: ").upper()
    if l in placeholder:
        print(f"You have already guessed {l}")
        continue
    j = 0
    for char in w1:
        if(l==char):
            placeholder = placeholder[:j]+l+placeholder[j+1:]
        j+=1
    if l not in w1:
        k+=1