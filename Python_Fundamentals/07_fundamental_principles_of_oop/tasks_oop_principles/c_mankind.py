import re
from abc import ABC,abstractmethod

class Human:
    @abstractmethod
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        if first_name[0] != first_name[0].upper():
            raise Exception('Expected upper case letter! Argument: firstName')
        elif len(first_name) <= 3:
            raise Exception('Expected length at least 4 symbols! Argument: firstName')

        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        if last_name[0] != last_name[0].upper():
            raise Exception('Expected upper case letter! Argument: lastName')
        elif len(last_name) <= 2:
            raise Exception('Expected length at least 3 symbols! Argument: lastName ')
        self.__last_name = last_name


class Student(Human):
    def __init__(self, first_name, last_name, faculty_number):
        Human.__init__(self, first_name, last_name)
        self.faculty_number = faculty_number

    @property
    def faculty_number(self):
        return self.__faculty_number

    @faculty_number.setter
    def faculty_number(self, faculty_number):
        is_allow = bool(re.match("^[0-9a-zA-z]*$",faculty_number))
        if len(faculty_number) < 5 or len(faculty_number) > 10 or not is_allow:
            raise Exception('Invalid faculty number!')
        self.__faculty_number = faculty_number

    def __str__(self):
        return f'First Name: {self.first_name}\nLast Name: {self.last_name}\nFaculty number: {self.faculty_number}'


class Worker(Human):
    def __init__(self, first_name, last_name, salary, working_hours):
        Human.__init__(self, first_name, last_name)
        self.salary = float(salary)
        self.working_hours = float(working_hours)

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if not (float(salary) > 10):
            raise Exception('Expected value mismatch! Argument: weekSalary')
        self.__salary = salary

    @property
    def working_hours(self):
        return self.__working_hours

    @working_hours.setter
    def working_hours(self, working_hours):
        if not(1 <= working_hours <= 12):
            raise Exception('Expected value mismatch! Argument: workHoursPerDay')
        self.__working_hours = working_hours

    def __str__(self):
        return f'First Name: {self.first_name}\nLast Name: {self.last_name}\nWeek Salary: {self.salary:.2f}\n' \
            f'Hours per day: {self.working_hours:.2f}\nSalary per hour: {self.salary / (self.working_hours*5):.2f}'




try:
    student_first_name,student_last_name, faculty_number = input().split()
    worker_first_name, worker_last_name, worker_salary, worker_hours = input().split()

    student = Student(student_first_name,student_last_name,faculty_number)
    worker = Worker(worker_first_name,worker_last_name,worker_salary,worker_hours)

    print(student)
    print()
    print(worker)
except Exception as exe:
    print(exe)
