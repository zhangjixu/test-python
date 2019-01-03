class Student(object):
    num_list = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.num_list)

    @classmethod
    def get_no_of_instance(cls):
        return cls.num_list

    @staticmethod
    def sum_count():
        print()
