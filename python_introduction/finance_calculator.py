monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

simple_annual_interest = 0.05

''' 
Use the simplified formula for annual savings projection: 
(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))
'''
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * simple_annual_interest)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")