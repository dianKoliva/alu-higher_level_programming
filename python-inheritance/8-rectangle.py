#!/usr/bin/python3
""" Module that defines a Rectangle class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines a Rectangle subclass of BaseGeometry """

    def __init__(self, width, height):
        """ Initializes a Rectangle object with width and height attributes

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
