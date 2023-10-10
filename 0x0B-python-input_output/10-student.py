#!/usr/bin/python3
"""A class Student definition"""
class Student:
    """Representation of the student"""

    def __init__(self, first_name, last_name, age):
        """Initialization of a new Student.

        Args:
            first_name: The first name of the student.
            last_name: The last name of the student.
            age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """the return is the dictionary representation of the Student

        Args:
            attrs: The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
