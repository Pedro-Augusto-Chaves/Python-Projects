# Instructions
# You are going to write a program that calculates the highest score from a List of scores.

# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# Important you are not allowed to use the max or min functions. The output words must match the example. i.e

# The highest score in the class is: x

scores = input("Digit the scores: ").split()
scores = list( map(int,scores) )
count = 0
highest_score = scores[0]

for score in scores:
    if scores[count]  > highest_score:
        highest_score = score
    count += 1

print(highest_score)
    


#armazena valor
#compara o valor atual com o antigo
#se o valor atual for maior, armazena o valor atual
#se não, deixa o valor antigo