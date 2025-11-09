#PASSWORD GENERATOR PROJECT
import random
letters = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']
print("Welcome to the PyPassword Generator!")
nl = int(input("How many letters would you like in your password?\n"))
ns = int(input("How many symbols would you like?\n"))
nn = int(input("How many numbers would you like?\n"))
  #Easy level --- in which first letters then symbols and numbers
password = ""
for i in range(nl):
    password+=random.choice(letters)
for i in range(ns):
    password+=random.choice(symbols)
for i in range(nn):
    password+=random.choice(numbers)
print("Easy Level Password:", password)
  #Hard level --- in which password does not have any pattern
password_list = []
for i in range(nl):
    password_list+=random.choice(letters)
for i in range(ns):
    password_list+=random.choice(symbols)
for i in range(nn):
    password_list+=random.choice(numbers)
random.shuffle(password_list)
password = ""
for char in password_list:
    password+=char
print("Hard Level Password:", password)