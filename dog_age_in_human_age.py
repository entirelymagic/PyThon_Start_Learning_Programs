while True:
    try:
        age = int(input("Enter the age of the dog: "))
        print()
        if age < 0:
            print("The age of your dog cannot be true")
        elif age == 0:
            print("Your dog is 0 years old")
        elif age == 1:
            print("Your dog is about 14 year old")
        elif age == 2:
            print("Your dog is about 22 years old")
        else:
            human_age = 22 + (age - 2) * 5
            print("Your dog is %d years old" % human_age)
    except ValueError:
        print("You have to introduce a number as an age!")
