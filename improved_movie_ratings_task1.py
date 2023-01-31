age = input("What is your age?")
if age.isdigit() and int(age) < 1 and int(age) > 117 :
    print("Please enter an age between 1 and 117")
elif age.isdigit() and int(age) >= 1 and int(age) < 8:
    print(f"You are {age} and are able to watch U rated films")
elif age.isdigit() and int(age) >= 8 and int(age) < 12:
    print(f"Your are {age} and are able to watch U and PG rated films")
elif age.isdigit() and int(age) >= 12 and int(age) < 15:
    print(f"Your are {age} and are able to watch U, PG and 12A rated films")
elif age.isdigit() and int(age) >= 15 and int(age) < 18:
    print(f"Your are {age} and are able to watch U, PG, 12A and 15 rated films")
elif age.isdigit() and int(age) >= 18:
    print(f"Your are {age} and are able to watch any film you like!")
else:
    print("Please enter a valid age using numbers between 1 and 117")

