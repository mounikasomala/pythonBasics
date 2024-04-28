# single inheritance
class box:
    def __init__(self,nameOfStudent,rollNo):
        self.nameOfStudent=nameOfStudent
        self.rollNo=rollNo

class box2(box):
    def __init__(self,marks):
        self.marks=marks
        box.__init__(self,"Raj",23)


obj2=box2(23)
print(obj2.marks)
print(obj2.nameOfStudent)
print(obj2.rollNo)
