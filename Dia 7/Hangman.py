import random

def find_letter():
    list_chosen_word = list(chosen_word)
    for i in range( len(list_chosen_word) ):
        if list_chosen_word[i] == letter_guess:
            guess_list[i] = letter_guess
        else:
            guess_list[i] = "_"
    return guess_list

##words to choose
word_list = ["aardvark", "baboon", "camel"]

##generate random word
chosen_word = random.choice(word_list)
guess_list = []
#create list with the lenght of the chosen world
for i in range( 0, len(chosen_word) ):
    guess_list.append('')

print(f"{guess_list} and {chosen_word}")

letter_guess = input("Guess one letter for the hangman game: ").lower()

find_letter()

if chosen_word.find(letter_guess) != -1:
    print("The letter is in the word.")
    print(guess_list)
else:
    print("The letter isn't in the word.")
    print(guess_list)



# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")


