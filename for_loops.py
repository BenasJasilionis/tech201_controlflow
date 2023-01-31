# Looping
# Cycle through a clause everytime our condition is met
# A for loop is where you define an iterator number and then cycle through data (list or dictionary) 'for each entry in that data structure.

# Creating a for loop

list_data = [1, 2, 3, 4, 5, 6]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

# num is just a placeholder, letting python know to go through every index in the list
# Every time the loop is initiated, the "num" placeholder is assigned to the data at the next index in the selected list, and that data then goes through the clause
# Best practice is to name the placeholder something relevant to the data to increase clarity
# Placeholder must be a variable ,so it can be assigned to the new index value with each loop- it cannot be a data type

# for num in list_data:
#     print(num * 2)

# nested for loops
# The first loop goes through each nested list within the list
# The nested for loop goes one layer deeper, and goes through each data point within the nested lists

# for data in embedded_lists:
#     print(data)
#     for num in data:
#         print(num)

# Loops for dictionaries
# This prints the key for every dictionary : value is assigned to the different keys with each loop
for value in dict_data:
    print(value)
# With dictionaries, you can use methods to get data out

for item in dict_data.values():
    print(item)

# Nesting a for loop outputs the data in a nicer way
# The first loop assigns each dictionary to the variable item
# The second nested loop assigns each value within the individual dictionaries to the variable embed_values and the end of the loop tells it to print each value out
#
# for item in dict_data.values():
#     print(item)
#     for embed_value in item.values():
#         print(embed_value)
#
for items in dict_data.values():
    print(items["money"])

# Please see Python documentation for more you can do with dictionaries and loops


# Loops and if statements

list_1 = [1, 2, 3, 4, 5]

for num in list_1:
    if num == 3:
        print("I found three")
    elif num > 3:
        print("Gone too far")
    else:
        print("Too soon")