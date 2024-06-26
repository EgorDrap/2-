grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grade = {'Aaron':(5, 3, 3, 5, 4), 'Khendrik':(2, 2, 2, 3), 'Steve':(4, 5, 5, 2), 'Bilbo':(4, 4, 3), 'Johnny':(5, 5, 5, 4, 5)}
print(grade)
a = grades[4]
b = grades[3]
c = grades [2]
d = grades [1]
e = grades [0]
aO=(sum(a)/len(a))
bO=(sum(b)/len(b))
cO=(sum(c)/len(c))
dO=(sum(d)/len(d))
eO=(sum(e)/len(e))
print({'Johnny':(eO), 'Bilbo':(dO), 'Steve':(cO), 'Khendrik':(bO), 'Aaron':(aO)})


#второй вариант
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = sorted(list(students))
print(students)
grades_ = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]
print(grades_)
A = dict(zip(students, grades_))
print(A)
