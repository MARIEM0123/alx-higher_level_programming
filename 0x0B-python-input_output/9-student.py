#!/usr/bin/python3
"""The class Student definition"""

class Student:
    """the class for  a student representation"""

    def __init__(self, first_name, last_name, age):
        """Initialization for a new Student

        Args:
            first_name: The first name 
            last_name: The last name of the student
            age: The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the Student"""
        return self.__dict__
