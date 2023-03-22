students = []

class Student:
    def __init__(self,name,surName) -> None:#constructor function
        self.name = name
        self.surName = surName
    
    def AddStudent(self):
        students.append(self.name +" "+ self.surName)#listeye öğrenci ekleme
        print("Öğrenci kaydedildi.") 

    def DeleteStudent(self):#listeden öğrenci silme
        for i in students:
            if(i == self.name +" "+ self.surName):
                students.remove(i)
                print("Öğrenci silindi")

            else:
                print("Öğrenci bulunamadı")

    def PrintStudents(self):#listedeki öğrencileri ekrana yazdırır
        return students

    def LearnNumber(self):#listedeki öğrenci sırasını verir index değil
        for i in students:
            print(i)
            if( i == self.name +" "+ self.surName):
                valueOfStudent=students.index(i)
                print("öğrenci {}.sırada".format(valueOfStudent+1))

    def DeleteStudents(self,StudentArray):
        for i in StudentArray:
            if i in students:
                students.remove(i)
        return students
    
    def AddStudents(self,StudentArray):
        for i in StudentArray:
            if not(i in students):
                students.append(i)
        return students
            
student1=Student("Hüseyin","Deneme")
student2=Student("Hüseyin","Deneme2")
student1.AddStudent()
student1.LearnNumber()
student1.DeleteStudents(["Hüseyin Deneme","Hüseyin Deneme2"])
student1.AddStudents(["Hüseyin Deneme","Hüseyin Deneme3"])
print(students)
