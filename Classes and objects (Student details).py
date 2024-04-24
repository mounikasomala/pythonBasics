class box:
    def __init__(self,currName,currrollnumber,currdbmsMarks,currosMarks,currjavaMarks,currdsMarks,currcMarks):
        self.name = currName
        self.rollnumber = currrollnumber
        self.dbmsMarks = currdbmsMarks
        self.osMarks = currosMarks
        self.javaMarks = currjavaMarks
        self.dsMarks = currdsMarks
        self.cMarks = currcMarks

#oblect creation
student1=box("Ram",354,90,98,87,95,81)
print(student1.name)
print(student1.rollnumber)
print(student1.dbmsMarks)

student2=box("sai",911,94,67,78,92,69)
print(student2.name)
print(student2.rollnumber)
print(student2.dbmsMarks)


student3=box("mouni",254,99,87,93,72,77)
print(student3.name)
print(student3.rollnumber)
print(student3.dbmsMarks)


student4=box("guna",555,93,82,94,84,83)
print(student4.name)
print(student4.rollnumber)
print(student4.dbmsMarks)
