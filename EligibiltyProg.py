def check_intern_eligibility(age,percentage):
  if age>=18 and percentage>=60:
      return 1
  else:
    return 0
age=int(input("Enter Age:"))
per=float(input("Enter Percentage:"))
res=check_intern_eligibility(age,per)
if res==1:
  print("Eligible\nAge is >=18 and percentage is >=60")
else:
  print("Not Eligible,Age should be >=18 and percentage should be >=60")
  
