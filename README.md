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
* `For` loops follow the following logic : `for each 
````
list_data = [1, 2, 3, 4, 5, 6]

for num in list_data:
    print(num * 2)
