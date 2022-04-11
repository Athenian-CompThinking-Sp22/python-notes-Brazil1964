#100 years old problem
from datetime import date

todays_date = date.today().year
try:
    currentAge = int(input("How old are you? "))
except ValueError:
    print("Not an integer! ")

year_turn = todays_date - currentAge + 100
print(f"You will be 100 years old in {year_turn}.")