m_income = int(input("Enter your monthly income: "))
m_expense = int(input("Enter your total monthly expenses: "))
m_savings = m_income - m_expense
projected_savings = int(m_savings * 12 + (m_savings * 12 * 0.05))  # Projected savings for one year
print(f"Your monthly savings are: ${m_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
