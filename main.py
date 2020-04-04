interestRate = 1.05
amount = 500 # by months
years = 40



def calculate(amount, interestRate, years):
  annualAmount = amount * 12
  result = 0
  for i in range(years):
    result = (result + annualAmount) * interestRate
    print('Amount per year', i, ' :', result)

  
