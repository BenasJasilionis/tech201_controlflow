user_inputs = []
final_list = []
count = 0
while count < 10:
    increment = int(input("Please type a number"))
    user_inputs += increment
    count += 1

print(len(user_inputs))
print(user_inputs)
for string in user_inputs:
    final_list.append(int(string))
print(final_list)
list_sum = sum(final_list)
print(list_sum / 10)