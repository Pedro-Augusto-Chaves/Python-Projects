print("Welcome!")

size = input("What size of pizza do you want? Small, Medium, Large or Family? ")
bill = 0

if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20
elif size == 'L':
    bill = 25

add_pepperoni = input("Dou want pepperoni in your pizza? Y or N: ")
if add_pepperoni == 'Y':
    bill += 2
    if size != 'S':
        bill += 1

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: {bill}")