while True:
    print()
    try:
        BM = float(input('Please insert the body mass of the person to calculate: \n'))
    except ValueError:
        print('You have to enter a number as the body mass')
    try:
        body_height = float(input('Please enter he height of the person to calculate: \n'))
    except ValueError:
        print('You have to enter a number as the height')
    BMI = BM / body_height**2
    print(f'BMI value is: {BMI}')
    if BMI < 15:
        print('You are very severely underweight!')
    elif BMI < 16:
        print('You are very severely underweight!')
    elif BMI < 18.5:
        print('You are underweight!')
    elif BMI < 25:
        print('You have a normal(healthy weight)!')
    elif BMI < 30:
        print('You are overweight!')
    elif BMI < 35:
        print('You are Obese class I(Moderately obese)')
    elif BMI < 40:
        print('You are Obese class II(Severely obese)')
    elif BMI < 45:
        print('You are Obese class III(Very severely obese)')
    elif BMI < 50:
        print('You are Obese class IV(Morbidly obese)')
    elif BMI < 60:
        print('You are Obese class V(Super obese)')
    elif 60 <= BMI:
        print('You are Obese class VI(Hyper obese)')
