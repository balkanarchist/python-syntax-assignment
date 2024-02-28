# If you have a savings account with a
# particular initial amount and a fixed
# yearly interest rate, calculate the total
# amount in your account after a year.

initial_amount = 500
interest_rate = 0.043 #4.3% converted to a decimal
years = 1
# account_value = amount in the account after one year
# The (modified for above) formula for calculating simple interest is:
# initial_amount * interest_rate (0.043) * years.

account_value = (initial_amount * interest_rate * years) + initial_amount
print(account_value)
