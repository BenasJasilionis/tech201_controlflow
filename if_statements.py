# Control Flow

# Allows us to make decisions based on the data
# Can be used individually or mixed together for more complex decisions
# Control flow -> to flow through a particular decision process.
# if statement - pass variables that meet criteria through clauses

age = 15

if age >= 18:
    print("You are the correct age to watch this film and can buy a ticket")



#if age < 18:
#    print(" I'm afraid you cannot watch this movie, you are not old enough")

# elif and else
film_rating = "16"

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
else:
    print("This is not a correct rating, please use universal, pg, 12, 15, 18")

# In Python there are no 'switch statements' or 'case statements'