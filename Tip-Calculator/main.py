print("Welcome to Tip calculator")
print('')
total_amount = int(input("Enter the total amount in your currency or in $"))
ques = int(input("Would u like to tip the server ? if yes then type 1: "))
print(' ')
if ques == 1:
  percent = int(input("Enter the amount of percentage u would like to give as tip? "))
  print('')
  split = int(input("Enter the amount of people u would like to split it with: "))
  print('')
  bill = total_amount / split
  billpercent = percent / 100
  total = bill * billpercent
  totalf = round(total , 2)
  print(f"The amount to be paid by each person is {totalf}")
else:
  split = int(input("Enter the amount of people u would like to split it with: "))
  print('')
  bill = total_amount / split
  totalf = round(bill, 2)
  print(f"The amount to be paid by each person is {totalf}")

