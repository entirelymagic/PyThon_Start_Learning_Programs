while True:
    gregorian = True
    try:
        year = int(input('Please introduce a year to see if it was a leap year: '))
        if year % 400 != 0 and year % 100 == 0:
            print('The year has 365 days because it is a centennial year divisible by 400')
        elif year % 4 == 0:
            print('This was a leap year and have 366 days.')
        else:
            print('The year has 365 days! Not a leap year.')
    except ValueError:
        print('You have to introduce a number!')
