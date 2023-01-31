# tech201_controlflow

# Control flow
* Allows us to make decisions based on the data
* Can be used individually or mixed together for more complex decisions
* Control flow -> to flow through a particular decision process by checking if our data meets certain conditions, and takinf different actions depending on what conditions are met


## IF statements
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
* `if` clauses can be expanded by adding `elif` which add extra criteria to look through if the first criteria isnt met