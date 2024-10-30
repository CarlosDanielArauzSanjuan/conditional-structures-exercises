# Solicitar al usuario que ingrese un año
year = int(input("Enter any year "))

# determinate if the year is a leap year
if year < 1582:
      # Julian calendar
    if year % 4 == 0:
        print(f"{year} is a leap year !!")
    else:
        print(f"{year} is not a leap year")
#  gregorian Calendar
else:  
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year !!")
    else:
        print(f"{year} is not a leap year")

