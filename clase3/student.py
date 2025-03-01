class Student:

    count = 0
    def _init_(self, name, age, language, city):
    #def init(self, name, age, language, city):
        self.name = name
        self.age = age
        self.language = language
        self.city = city
        Student.count += 1

    def _str_(self):
    #def str(self):
        return f"Name: {self.name}, Age: {self.age}, Language: {self.language}, City: {self.city}"

    @staticmethod
    def get_total_students():
        return Student.count

    @classmethod
    def get_total_students_class(cls):
        return cls.count


if _name_ == '_main_':
    estudiante = Student('Juan',20, 5, 'madrid')
    print(Student.get_total_students())
    print(Student.get_total_students_class())

    estudiante.name = 'Juan'
    # print(estudiante)

    estudiante2 = Student('Eduardo', 30, 7, 'madrid')
    print(Student.get_total_students())
    print(Student.get_total_students_class())