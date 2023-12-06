#!/usr/bin/python3
"""Defines a Rectangle  class  that inherits from BaseGeometry."""


class Rectangle(BaseGeometry):
    """represent Rectangle class"""
    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
