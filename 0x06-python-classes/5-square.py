#!/usr/bin/python3
"""a square"""


class Square:
    """class square"""
    def __init__(self, size=0):
        self.__size = size
    """def class"""
    @property
    def size(self):
        return self.__size
    """def class"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value
    """def class"""
    def area(self):
        return self.__size * self.__size
    """def class"""
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("{}".format("#"), end="")
            print()
