class Student(object):
    def __init__(self):
        self.RollNo=""
        self.Name=""
        self.CourseNames=[]

    def GetRollNo(self, RollNo):
        return self.RollNo
    def GetName(self, Name):
        return self.Name
    def AddCourseName(self,coursename):
        return self.CourseNames(coursename)