# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
import random

names_string = input("Write the names: ")

names = names_string.split(", ")

random_number = random.randint(0, len(names)-1 )

random_name = names[random_number]

print(f"{random_name} IS GOING TO BUY THE MEAL TODAY!")