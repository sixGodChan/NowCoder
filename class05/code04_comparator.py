# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi

class Student():
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

    def __lt__(self, other):
        return self.age < other.age


if __name__ == '__main__':
    student1 = Student('A', 1, 40)
    student2 = Student('B', 2, 21)
    student3 = Student('C', 3, 12)
    student4 = Student('D', 4, 62)
    student5 = Student('E', 5, 42)
    lst = [student1, student2, student3, student4, student5]

    # 实例对象比较 __lt__函数
    print(student1 < student2)

    print([(i.name, i.id, i.age) for i in lst])
    lst.sort()
    print([(i.name, i.id, i.age) for i in lst])

    # 实例对象排序 方式1 lambda
    lst.sort(key=lambda x:x.id, reverse=False)
    print([(i.name, i.id, i.age) for i in lst])

    # 实例对象排序 方式2 attrgetter
    from operator import attrgetter

    lst.sort(key=attrgetter('age'))  # attrgetter('age', 'id')
    print([(i.name, i.id, i.age) for i in lst])