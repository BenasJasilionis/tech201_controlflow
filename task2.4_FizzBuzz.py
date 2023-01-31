count = 1

while count <= 100:
    if (count % 3) == 0 and (count % 5) == 0:
        print(f"{count} FizzBuzz")
        count += 1
        continue
    elif (count % 3) == 0:
        print(f"{count} Fizz")
        count += 1
    elif (count % 5) == 0:
        print(f"{count} Buzz")
        count += 1
    else:
        print(count)
        count += 1
