# tech201_controlflow

# Control flow
* Allows us to make decisions based on the data
* Can be used individually or mixed together for more complex decisions
* Control flow -> to flow through a particular decision process by checking if our data meets certain conditions, and taking different actions depending on what conditions are met


# IF statements
* `if` statements allow us to pass variables through several criteria, and then take action depending on what criteria is met
* For instance `if x = z then do y`
* In a more technical sense the syntax would look like this :
````
age = 15

if age >= 18:
    print("You are the correct age to watch this film and can buy a ticket")
````
* Here we see that the variable `age` is defined as 15
* The `if` statement check if `age >= 18` and if so it prints the specified string
* If the condition isn't met, nothing happens
* **Note how everything in the `if` clause is indented to show that it is part of that clause**

# ELIF and ELSE
* `if` clauses can be expanded by adding `elif` which add extra criteria to look through if the first criteria isn't met
* Each `elif` clause is exactly the same as writing another if clause, but instead of writing another `if` clause it allows us to expand the current one:
````
film_rating = "18"

if film_rating.lower() == "universal":
    print("All age groups can watch this film")
elif film_rating.lower() == "pg":
    print("Genetal viewing but parental guidance advised")
elif film_rating.lower() == "12" or film_rating == "12a":
    print("12 rated movies may not be suitable for those under 12, supervision is recommended")
elif film_rating.lower() == "15":
    print("You must be 15 to watch 15 rated movies in the cinema")
elif film_rating.lower() == "18":
    print("You must be 18 to watch 18 rated movies in the cinema")
````
* The above example showcases how we can add as many `elif` statements as we like to our `if` clause.
* At each step, the variable in question will be evaluated against the target, and if the condition isn't met, the program will proceed to the next clause.
* Once a condition is met, the associated `if` or `elif` instruction will be carried out and the program will end
* For example : `film_rating = 18` would output `You must be 18 to watch 18 rated movies in the cinema`

### ELSE
````
else:
    print("This is not a correct rating, please use universal, pg, 12, 15, 18")
````
* An `else` statement can be added to carry out a command if no other `if` or `elif` condition is met
* Because `else` is used when no condition is met and is used to end an `if` clause, it does not need its own condition to initiate
* Notice how the `print` statement is embedded after `else:` - embedding commands correctly is crucial in maintaining a functional control flow.

# For loops
* A `for` loop is where you define an iterator number and then cycle through data (list or dictionary) 'for each entry in that data structure
* For instance, if a list has 5 entries, 5 loops will be completed
* With each iteration, the `for` loop can be instructed to carry out a task or print an output
* `For` loops follow the following logic : `for each "thing" in x data set, do y`

An example can be seen below:
````
list_data = [1, 2, 3, 4, 5, 6]

for num in list_data:
    print(num * 2)
````
* `num` is just a placeholder, letting python know to go through every index in the list
* Every time the loop is initiated, the `num` placeholder is assigned to the data at the next index in the selected list, and that data then goes through the clause
* Best practice is to name the placeholder something relevant to the data to increase clarity
* Placeholder must be a variable ,so it can be assigned to the new index value with each loop- it cannot be a data type
1) In the first loop, `num` takes the value of index 0, which is 1. The next part of the program says to do `num * 2` or in other words `1 * 2` which outputs `2`
2) In the second loop, `num` is now assigned the 1st index, which is 2, so the program runs `2 * 2` which is `4`
3) This process carries on until the `for` loop runs out of indexes in the data set, so the final output will read : `2, 4, 6, 8, 10, 12`

### For loops with nested lists
* Data can be stored in more complex ways, such as lists within lists which are called nested lists.
* To access the data within these lists, a nested `for` loop is needed
* The first loop goes through each nested list within the list
* The nested `for` loop goes one layer deeper, and goes through each data point within the nested lists
````
embedded_lists = [[1, 2, 3], [4, 5, 6]]

for data in embedded_lists:
    print(data)
    for num in data:
        print(num)
````
1) The first line instructs the program to go through every nested list within the big list called `embedded_lists`. We can see that there are two, which means that this `for` loop will run twice.
2) In the second line, the program is told to print the data at index 0, this will output the first list `[1, 2, 3]`
3) The third line initiates a nested `for` loop, which instructs the program to iterate through the data within the nested lists
4) Because we are still in the first loop, the program will now iterate through the first nested list 3 times due to there being 3 items
5) The final line tells the program to print an object after each iteration, and because there are 3 iterations, each covering a different index in the list, this will out put : `1, 2, 3` on separate lines
6) The loop will go to the beginning now, and move on to the second nested list and do steps 2-5 on it, after which it will end.

**It is very important to take note of the indentation when embedding for loops**

### For loops with dictionaries
`For` loops can be used to get data out of dictionaries, and listed dictionaries in the same was as lists
````
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

for value in dict_data:
     print(value)
````
1) As discussed, `for` loops work from the outside in with each embedded loop, therefore running the code above will iterate through the big dictionary, returning the keys for the embedded dictionaries : `1, 2, 3
````
for item in dict_data.values():
      print(item)
````
2) Dictionaries allow for the use of methods to get data out, for instance the `.values()` seen above will return the key value pairs for all the dictionaries, however the formatting is suboptimal
````
 for item in dict_data.values():
     print(item)
     for embed_value in item.values():
         print(embed_value)
````
3) Here as before, the first 2 lines instruct the program to iterate through the big dictionary and print out the key value pairs found within the embedded dictionaries
4) The embedded `for` loop tells the program to iterate through each embedded dictionary, and to print out only the values, not the key:value pairs
````
for items in dict_data.values():
     print(items["money"])
````
5) We can also request values from specific keys.
6) The first line iterates through all the key value pairs using the `,values()` method.
7) The second line tells the program to print only the values for the key money with the syntax : `print(items["money"])`

### For loops and if statements
For loops and if statements can be combined for more complex programs. Below is a simple example:
````
list_1 = [1, 2, 3, 4, 5]

for num in list_1:
    if num == 3:
        print("I found three")
    elif num > 3:
        print("Gone too far")
    else:
        print("Too soon")
````
1) The `num` tells the loop to iterate through the list `list_1` once for every item in the list, meaning there will be 5 iterations
2) The first `if` clause tells the program to print `I found three` if the currently iterated value is `3`
3) The `elif` clause tells the program to print `Gone too far` if the iterated number is a higher value then 3
4) Finally, the else clause tells the program to print `Too soon`, and this will only happen if the iterated number is less than 3