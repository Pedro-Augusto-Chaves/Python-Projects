import random
import Hangman_words
import Hangman_images

lives = 6

#Funcion to write the right letter in the word
def find_letter():
    for i in range( len(list_chosen_word) ):
        if list_chosen_word[i] == letter_guess:
            guess_list[i] = letter_guess
    return guess_list

print(Hangman_images.logo)

#Choose one random word from the words list
word_list = Hangman_words.word_list
chosen_word = random.choice(word_list)
list_chosen_word = list(chosen_word)

#Create list with the lenght of the chosen world and a list to store repeated letters
guess_list = []
for i in range( 0, len(chosen_word) ):
    guess_list.append('_')
repeated_letters = []


#Loop to ask the guess letter and perfom the game
while guess_list != list_chosen_word and lives != 0:
    letter_guess = input("Guess one letter for the hangman game: ").lower()
    
    #check if the letter is in the word
    if repeated_letters.count(letter_guess) != 0:
        print("\nYou already chose this letter. \n")
        print( ''.join(guess_list) + '\n')

    elif chosen_word.find(letter_guess) != -1:
        find_letter()
        print( ''.join(guess_list) + '\n')

    else:
        lives -= 1

        print(f"\nThe letter {letter_guess} isn't in the word. \n")
        print(Hangman_images.stages[lives])
        print( ''.join(guess_list) + '\n' )

    repeated_letters.append(letter_guess)

#Condition to win
if lives == 0:
    print("You lost!")
else:
    print("You won! Congrats")





# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")


