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
