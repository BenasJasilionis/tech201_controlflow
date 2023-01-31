hours_worked = float(input("How many hours have you worked this week?"))
hourly_rate = float(input("How much do you get payed per hour?"))

if hours_worked <= 40:
    print(f"You have earned £{hours_worked * hourly_rate} this week")
elif hours_worked > 40:
    regular_wage = hours_worked * hourly_rate
    overtime = (hours_worked - 40) * (hourly_rate * 1.5)
    total_wage = overtime + regular_wage
    print(f"You have earned £{total_wage} this week")

