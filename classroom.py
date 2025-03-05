#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 10:13:14 2025

@author: hugoo
"""

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def get_name(self):
        return str(f"This person is called {self.firstname} {self.lastname}")

#testing the person class    
#p1 = Person('Hugo', 'Olsson')
#print(p1.get_name())

class Student(Person):
    def __init__(self, firstname, lastname, subject):
        Person.__init__(self, firstname, lastname)
        self.subject = subject
    def get_name_and_subject(self):
        return str(f"This person is called {self.firstname} {self.lastname} and studies {self.subject}")
    
class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        Person.__init__(self, firstname, lastname)
        self.course = course
    def get_name_and_course(self):
        return str(f"This person is called {self.firstname} {self.lastname} and teaches {self.course}")