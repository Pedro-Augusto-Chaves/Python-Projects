# Prime numbers are numbers that can only be cleanly divided by themselves and 1.

# https://en.wikipedia.org/wiki/Prime_number

# You need to write a function that checks whether if the number passed into it is a prime number or not.

# e.g. 2 is a prime number because it's only divisible by 1 and 2.

# But 4 is not a prime number because you can divide it by 1, 2 or 4.
def discover_prime_number(number_input):
    prime = True
    for number in range(2,number_input):
        rest = number_input % number
        if rest == 0:
            prime = False
            
    if prime:
        print("Its a prime number")
    else:
        print("isnt a prime number")

counter = 0
while counter != 100:
    number_input = int( input("Digit the number: ") )    
    discover_prime_number(number_input)
    counter += 1