from math import sqrt

while True:
    try:
        n = int(input('Maximum number? '))
    except ValueError:
        print('You must enter a valid number!')
    for a in range(1, n+1):
        for b in range(a, n):
            c_squared = a**2 + b**2
            c = int(sqrt(c_squared))
            if (c_squared - c**2) == 0 and c <= n:
                print(a, b, c)
