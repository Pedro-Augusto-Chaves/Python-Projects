# Write a program that adds the digits in a 2 digit number. 
# e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input()

if int(two_digit_number) and 9 < int(two_digit_number) < 100:
    first_number = int(two_digit_number[0])
    second_number = int(two_digit_number[1])
    print(first_number + second_number)