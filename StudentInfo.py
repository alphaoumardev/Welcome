class StudentInfo:
    numberOfStudent = 21

    def __init__(self, name, age, gender, studentId):
        self.name = name
        self.age = age
        self.gender = gender
        self.studentId = studentId

    def information(self):
        print("The student informations are name:{},age: {}, gender: {}, studentInfo:{}".format(self.name, self.age,
                                                                                                self.gender,
                                                                                                self.studentId))


com = StudentInfo("AlphaOumar", 21, "female", 16)
com.information()
