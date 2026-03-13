price = 0
onehours = 0
hours = int(input("add the numbers of hours you spent in the parking lot: "))
if hours == 0:
    price = 0
elif hours == 1:
    price = 5000
else:
    onehours = 5000
    price = 3000
total = ((hours-1)* price + onehours)
print("the total price is: ", total)

