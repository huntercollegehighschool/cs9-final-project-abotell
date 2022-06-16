"""
Name(s): Ana Botella
Name of Project: hangman
"""
import random

print("Welcome to Hangman. You have 10 mistakes before you fail the game.")

from page1 import words
word = random.choice(words)

word_letters = list(word)
used_letters = set()
blanks = ["_"] * len(word_letters)
word_letters = list(set(word_letters)) 
#print(word_letters)
#print(word)


print(blanks)
guess = 9


user_letter = input("Guess a letter: ")
#print(word)
while len(word_letters) > 0 and guess > 0:
  if user_letter not in used_letters:
    used_letters.add(user_letter)
    for i in range(len(word)):
      if user_letter == word[i]:
        blanks[i] = user_letter
    if user_letter in word_letters:
      word_letters.remove(user_letter)
      print("That letter was in the word!")
      if len(word_letters) == 0:
        print("You did it! The word was", word)
      else:
        print(blanks)
        print("You have used these letters:", used_letters)
        print("You have", guess + 1, "mistakes left.")
        user_letter = input("Guess a letter: ")
    else:
      print(blanks)
      guess -= 1
      print("That was wrong. You have used these letters:", used_letters)
      print("You have", guess + 1, "mistakes left.")
      user_letter = input("Guess a letter: ")
  else:
    print(blanks)
    user_letter = input("you have already used that letter. Try again: ")
if guess == 0:
  print("That was wrong.")
  print("You have taken too many guesses. The word was", word, "and you have failed.")
