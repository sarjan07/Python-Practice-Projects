import random

names_string = input("Give me everybody's names, seperated by the comma. \n")
names = names_string.split(", ")

# Get teh total number of item in list.
# num_items = print(len(names))
#
# random_choice = random.randint(0, 'num_items'-'1')
# person_who_will_pay = print(random_choice)



person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to the buy the today's meal!")


# Using str.split is directly convert lists from the string using str.split(',')