# This program estimates a user's typical food expenditure.

times_at_cafteria = int(input("How many times a week do you eat at the cafteria? "))
launch_price = float(input("The price of a typical student launch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))

weekly_spent = times_at_cafteria * launch_price
total_weekly_spending = weekly_spent + groceries
daily_total = total_weekly_spending / 7

print(f"Average food expenditure:")
print(f"Daily: {daily_total} euros")
print(f"Weekly: {total_weekly_spending} euros")