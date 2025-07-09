# This program asks the number of students on a course and the desired group size, the program then print out the number of the groups formed from the students on the course.

total_students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

groups = total_students // group_size

if total_students % group_size !=0:
    groups += 1
print(f"Number of groups formed: {groups}")