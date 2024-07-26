students_height = input("Input a list of student heights \n").split()
for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
print(students_height)
# total_height = sum(students_height)
# number_of_students = len(students_height)

total_height = 0
for height in students_height:
    total_height += height

number_of_students = 0
for student in students_height:
    number_of_students += 1
print(f"The number of student is {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"The average height of the student is {average_height} Cm")
