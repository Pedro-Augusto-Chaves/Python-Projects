year = int( input("Digite the year you want to know if is a leap year: ") )

if year%4 == 0:
    if year%100 != 0:
        print("Its a leap year")
    elif year%400 == 0:
        print("Its a leap year")
    else:
        print("Isn't a leap year")
else:
    print("Isn't a leap year")
    