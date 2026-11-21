# class methods = allows operations related to the class itself

class student:

    count = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score
        student.count += 1

    @classmethod
    def get_info(cls):
        return cls.count


student1 = student("Ali", 90)
student2 = student("Mohammed", 100)

print(student.get_info())