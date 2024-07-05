name1 = input("Digit the first name: ")
name2 = input("Digit the second name: ")
true_appearences = 0
love_appearences = 0


for i in range( len(name1) ):
    if name1[i] == 'T' or name1[i] == 'R' or name1[i] == 'U' or name1[i] == 'E':
        true_appearences += 1

for i in range( len(name1) ):
    if name1[i] == 'L' or name1[i] == 'O' or name1[i] == 'V' or name1[i] == 'E':
        love_appearences += 1

true_love_appearences = str(true_appearences) + str(love_appearences)


for i in range( len(name2) ):
    if name2[i] == 'T' or name2[i] == 'R' or name2[i] == 'U' or name2[i] == 'E':
        true_appearences += 1

for i in range( len(name2) ):
    if name2[i] == 'L' or name2[i] == 'O' or name2[i] == 'V' or name2[i] == 'E':
        love_appearences += 1

true_love_appearences = str(true_appearences) + str(love_appearences)
true_love_appearences = int( true_love_appearences )

if true_love_appearences < 10 and true_love_appearences > 90:
    print(f"Your score is {true_love_appearences}, you go together like coke and mentos.")
elif true_love_appearences >= 40 and true_love_appearences <= 50:
    print(f"Your score is {true_love_appearences}, you are alright together.")
else:
    print(f"Your score is {true_love_appearences}.")
