#Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

number_letters = int( input("How many letters would you like in your password?\n") ) 
number_symbols = int( input(f"How many symbols would you like?\n") )
number_numbers = int( input(f"How many numbers would you like?\n") )


total_characters = number_letters + number_symbols + number_numbers

password = []
counter = 0

for x in range(1 , total_characters+1):
    random_letter = random.choice(letters) #escolhe um valor aleatório de uma sequência
    random_symbols = random.choice(symbols)
    random_numbers = random.choice(numbers)

    if counter < number_letters:   
        password.append(random_letter)
    elif counter < number_symbols + number_letters:
        password.append(random_symbols)
    else:
        password.append(random_numbers)
    
    counter += 1



random.shuffle( password )
password = ''.join(password)

print(f"Here is your password: {password}")
    
#Método mais eficiente
# for _ in range(number_letters):
#     password.append(random.choice(letters))

# # Adiciona símbolos
# for _ in range(number_symbols):
#     password.append(random.choice(symbols))

# # Adiciona números
# for _ in range(number_numbers):
#     password.append(random.choice(numbers))