# # his is a difficult challenge. 💪

# # You are going to write a program that will mark a spot on a map with an X.

# # In the starting code, you will find a variable called map.

# # This map contains a nested list. When map is printed this is what it looks like, notice the nesting:
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

row1 = ["", "", ""]
row2 = ["", "", ""]
row3 = ["", "", ""]

map = [row1, row2, row3]

position = list( input("Insert the position you want to hide the treasure: ") )

letter = ['a','b','c']
number = ['1','2','3']

index_letter = letter.index(position[0].lower())
index_number = number.index(position[1])

map[index_number][index_letter] = 'X'


print(f"{row1}\n{row2}\n{row3}")
