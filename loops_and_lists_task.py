# # Task 1
# # for i in range(0,10):
# #     print("Hello")
#
# # Task 2
# name_list = []
# for i in range(0,5):
#     name = input("What is your name?")
#     name_list.append(name)
# #print(name_list)
#
# # Task 3
# list_names_lower = []
# for name in name_list:
#     list_names_lower.append(name.lower())
# #print(list_names_lower)

# Extra task 1
# count = 0
# total = 0
# while count <= 100:
#     total += count
#     count += 1
# print(total)

#Extra task 2
count = 0
even_count = 0
odd_count = 0
while count <= 100:
    if (count % 2) == 0:
        even_count += count
    else:
        odd_count += count
    count += 1
print(even_count)
print(odd_count)

