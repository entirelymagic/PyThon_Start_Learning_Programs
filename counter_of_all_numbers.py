from datetime import datetime


while True:
    try:
        total_sum = 0
        counter = 1
        number = int(input('Please introduce a positive number: \n'))
        earlier = datetime.now()
        while counter <= number:
            total_sum += counter
            counter += 1
        now = datetime.now()
        total_time_passed = now - earlier
        print(f"Sum of 1 until {str(number)} is {str(total_sum)} nad was calculated in {str(total_time_passed)}")
    except ValueError:
        print('You have to introduce a number!')