m_income = int(input("Enter your monthly income: "))
m_expense = int(input("Enter your total monthly expenses: "))
m_savings = m_income - m_expense
projected_savings = m_savings * 12 + (m_savings * 12 * 0.05)  # Projecting savings for 5 years
print(f"Your monthly savings are: ${m_savings}")
print(f"Projected savings after 5 years: ${projected_savings}")