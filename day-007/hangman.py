#Step 1
import random
import hangman_art
import word_list

word_list = word_list.word_list
stages = hangman_art.stages
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
output_letter = []
letter = random.choice(word_list)
largo = len(letter)
[output_letter.append("_") for l in range(0, largo)]
print(output_letter)
print(hangman_art.hangman)
lives = 6
while output_letter.count("_") != 0 and lives > 0:
      letra = input('Ingrese una letra!\n').lower()
      i = 0
      for l in letter:
          if l == letra:
              output_letter[i] = letra
          i += 1
      print(output_letter)
      if letra not in letter:
          lives -= 1
          print(stages[lives])
          print(lives)
        


if lives == 0:
  print("You Loose...")
else:
  print("You WIN...")