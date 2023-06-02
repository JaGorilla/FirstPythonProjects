import random, hangman_art, hangman_words
from replit import clear

play_again = False

while not play_again:
  chosen_word = random.choice(hangman_words.word_list)
  word_length = len(chosen_word)
  
  end_of_game = False
  lives = 6
  
  print(hangman_art.logo)
  
  #Create blanks
  display = []
  past_guesses = []
  for _ in range(word_length):
      display += "_"
  
  while not end_of_game:
      guess = input("Guess a letter: ").lower()
      clear()
  
      #Check if user is wrong.
      if guess not in chosen_word and guess not in past_guesses:
          print('Sorry. That letter is not in the word.\n')
          lives -= 1
          print(hangman_art.stages[lives])
          print(f"{' '.join(display)}")
          if lives == 0:
              end_of_game = True
              print(f'You lose. The word was "{chosen_word}."\n')
              #print(hangman_art.stages[lives])
  
      # Check if user is right.
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess and guess not in past_guesses:
              print('Nice guess!\n')
              print(hangman_art.stages[lives])
              display[position] = letter
              print(f"{' '.join(display)}")
  
      # Check if guess is duplicate     
      if guess in past_guesses:
        print('You have already guessed that letter. Guess a different letter.\n')
        print(hangman_art.stages[lives])
        print(f"{' '.join(display)}")
      else:
        past_guesses += guess
  
      #Join all the elements in the list and turn it into a String.
  
      #Check if user has got all letters.
      if "_" not in display:
          end_of_game = True
          print("You win!\n")