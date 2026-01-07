def check_password_strength(password):
  if len(password)<8:
    print("Weak Password\nNumber of character is less than 8")
  spe="!@#$%^&*()_+=-{}[]:'<>?/~"
  spe1=any(i in spe for i in password)
  dig=any(i.isdigit() for i in password)
  if len(password)>=8 and dig and spe1:
    print("Strong Password")
  else:
    print("Password must contain a digit and special character")
password=input("Enter a Password")
a=check_password_strength(password)
print(a)
