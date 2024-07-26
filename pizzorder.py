# This is mini pizza restraunts 

small_price = 55
meduim_price = 80
large_price = 100

extra_cheese = 30
extra_peporeni = 15

bill = 0
isvalid = 1

print("We have three diffrenet types of pizza such as small,meduim and large")
user_choice = input("Enter your pizza type s,m,l ")
extra_cheese_ = input("Do you want to add extra cheese  y or n? ")
extra_peporeni_ = input("Do you want to add extra peporeni y or n? ")
 
if user_choice == 's':
    bill += small_price
elif user_choice == 'm':
    bill += meduim_price
elif user_choice == 'l':
    bill += large_price
else:
    print("Please enter valid input")
    isvalid = 0
    
if extra_cheese_ == 'y':
    bill += extra_cheese
elif extra_cheese_== 'n':
    pass
else:
    isvalid = 0

if extra_peporeni_ == 'y':
    bill += extra_peporeni
elif extra_peporeni_ == 'n':
    pass
else:
    isvalid = 0
    
if isvalid:
    bill += bill * 0.12
    bill = round(bill, 0)
    print(f"your pizza is ready having price is Rs. {bill}")
else:
    print("Please enter valid input")