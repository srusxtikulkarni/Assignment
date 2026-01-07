def calculate_electricity_bill(units):
  if units<100:
    bill=units*2
  elif units>100 and units<200:
    bill=units*4
  elif units>200:
    bill=units*6
  return bill
units=float(input("Enter number of units:"))
tot_bill=calculate_electricity_bill(units)
print("Total Bill:",tot_bill)
