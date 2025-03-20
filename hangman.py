import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
         word = random.choice(words)
    
    return word.upper()

def hangman():
     word = get_valid_word(words)
     word_letters = set(word)
     used_letters = set()
     alphabet = set(string.ascii_uppercase)
     
     lives = 6

     while len(word_letters) > 0 and lives > 0 :
         #letters used
         #' '.join(['a', 'b','cd'])
         print(f"You have",lives," lives left and you have used these letters: " , " ".join(used_letters))
         #what current word is (ie W - R D)
         word_list = [letter if letter in used_letters else '-' for letter in word]
         print('Current word: ',' '.join(word_list))

         user_letter = input("Guess a letter:").upper()
         if user_letter in alphabet - used_letters:
             used_letters.add(user_letter)
             if user_letter in word_letters:
                  word_letters.remove(user_letter)
             else:
                   lives = lives-1
                   print("This letter is not in the word")

         elif user_letter in used_letters:
              print("You've used that letter already. Please try again....")
        
         else:
              print("Invalid character.Please try again")
     if lives == 0:
           print(f"Sorry' you died. The word is {word}") 
     else:
           print(f"Yay, You've guessed the word. The current word {word}")
                       
hangman()
