#CAESAR CIPHER (A CODE WHERE ENCRYPTION AND DECRYPTION OF MESSAGES IS DONE)
import string
def encrypt(text, shift):
    cipher_txt = ""
    for i in range(len(text)):
        if text[i] in symbols:
            cipher_txt+=text[i]
            continue
        if(text[i].isdigit()):
            cipher_txt+=text[i]
            continue
        if(text[i]==" "):
            cipher_txt+=text[i]
            continue
        index = alphabet.index(text[i])
        index+=shift
        index%=len(alphabet) #this for when index exceeds the range of the list it gets it from the starting ex: if have index=34 so 34%25 we get 9 so from starting 9th letter will be printed
        cipher_txt+=alphabet[index]
    print(cipher_txt)

def decrypt(text, shift):
    decoded_txt = ""
    for char in text:
        if char in symbols:
            decoded_txt+=char
            continue
        if(char.isdigit()):
            decoded_txt+=char
            continue
        if(char==" "):
            decoded_txt+=char
            continue
        index = alphabet.index(char)
        index-=shift
        index%=len(alphabet)
        decoded_txt+=alphabet[index]
    print(decoded_txt)

logo = '''
                                                                                                                                     
  ,ad8888ba,                                                             ,ad8888ba,  88             88                                 
 d8"'    `"8b                                                           d8"'    `"8b ""             88                                 
d8'                                                                    d8'                          88                                 
88            ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,    88            88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
88            ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8    88            88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
Y8,           ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88            Y8,           88 88       d8 88       88 8PP""""""" 88          
 Y8a.    .a8P 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88             Y8a.    .a8P 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
  `"Y8888Y"'  `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88              `"Y8888Y"'  88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                                                                                        88                                             
                                                                                        88                                             '''
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = string.punctuation #this contain all the special symbols !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
rewrite = 'yes'
while(rewrite=='yes'):
    dir = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if(dir=='encode'):
        encrypt(text, shift)
    elif(dir=='decode'):
        decrypt(text, shift)
    rewrite = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
