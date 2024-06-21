#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float( input("Digit the bill: ") )
tip_percentage = int( input("Digit the tip percentage between 10, 12 or 15 percent: ") ) / 100
total_bill = bill + (bill * tip_percentage)

number_people = int( input("How much people will split the bill: ") )
bill_per_person = total_bill/number_people 
 
print(bill_per_person)
print(f"Each person will pay R$ {bill_per_person:.2f}")