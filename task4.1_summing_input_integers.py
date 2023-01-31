user_inputs = []
final_list = []
count = 0
while count < 10:
    increment = input("Please type a number")
    user_inputs.append(increment)
    count += 1

#print(len(user_inputs))
#print(user_inputs)
for string in user_inputs:
    final_list.append(int(string))
#print(final_list)
list_sum = sum(final_list)
print(f"The average value of the 10 you provided is: {list_sum / 10}")