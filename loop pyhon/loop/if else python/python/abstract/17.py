# 17. Online Course Platform
# Course
# ProgrammingCourse
# PythonCourse

# Add certification system.

class Course:
    def courseInfo(self):
        print("Course started")

class ProgrammingCourse(Course):
    def programming(self):
        print("Programming course is available")

class PythonCourse(ProgrammingCourse):
    def certificate(self):
        print("Python course certificate awarded")

p = PythonCourse()

p.courseInfo()
p.programming()
p.certificate()