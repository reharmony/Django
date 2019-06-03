class Student:
    math = 0
    eng = 0
    avg_math = 0
    avg_eng = 0
    sum_math = 0
    sum_eng = 0
    count = 0

    def __init__(self, math, eng):
        self.math = math
        self.eng = eng
        Student.count = Student.count + 1
        Student.sum_math = Student.sum_math + math
        Student.avg_math = Student.sum_math / Student.count
        Student.sum_eng = Student.sum_eng + eng
        Student.avg_eng = Student.sum_eng / Student.count

    def __str__(self):
        return '수학: ' + str(self.math) + "  영어: " + str(self.eng)



a = Student(70, 80)
b = Student(90, 85)
c = Student(85, 95)

print('학생a =', a)
print('학생b =', b)
print('학생c =', c)
print('수학 총점:', Student.sum_math)
print('수학 평균:', Student.avg_math)
print('영어 총점:', Student.sum_eng)
print('영어 평균:', Student.avg_eng)
