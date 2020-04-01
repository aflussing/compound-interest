interestRate = 1.05
amount = 500 # by months
years = 40
result = 0
annualAmount = amount * 12

for i in range(years):
  result = (result + annualAmount) * interestRate
  print('Amount per year', i, ' :', result)
