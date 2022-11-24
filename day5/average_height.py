students_heights = input("Enter the lists of heights").split()
for n in range(0,len(students_heights)):
    students_heights[n]= int(students_heights[n])
print(students_heights)

total_height=0
for height in students_heights:
    total_height+=height
print(total_height)

number_of_students = 0
for student in number_of_students:
    number_of_students+=1

average_height = (total_height/number_of_students)
print("The average height is ", average_height)
