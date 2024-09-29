grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
a = (sum(grades[0]))/(len(grades[0]))
b = (sum(grades[1]))/(len(grades[1]))
c = (sum(grades[2]))/(len(grades[2]))
d = (sum(grades[3]))/(len(grades[3]))
e = (sum(grades[4]))/(len(grades[4]))
grades1 = [a, b, c, d, e]

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students))
student1 = {students[0]:grades1[0]}
student2 = {students[1]:grades1[1]}
student3 = {students[2]:grades1[2]}
student4 = {students[3]:grades1[3]}
student5 = {students[4]:grades1[4]}
GPA = {**student1, **student2, **student3, **student4, **student5}
print(GPA)