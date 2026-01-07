def calculate_discount(price,customer_type):
  if price<0:
    print("Enter appropriate price")
  if customer_type=="Regular":
    dis=price*5/100
    print("Final Price",price-dis)
  elif customer_type=="Premium":
    dis=price*15/100
    print("Final Price",price-dis)
  elif customer_type=="Employee":
    dis=price*25/100
    print("Final Price",price-dis)
user=int(input("Enter the price"))
customer_type=input("Enter Customer type")
calculate_discount(user,customer_type)
