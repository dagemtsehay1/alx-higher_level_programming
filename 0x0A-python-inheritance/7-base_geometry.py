#!/usr/bin/python3
'''Documentaion'''


class BaseGeometry():
    ''''Basic class'''
    def area(self):
        '''Method no implements yet'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validates right input'''
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
