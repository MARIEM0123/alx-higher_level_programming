#!/usr/bin/python3
"""The class MyInt inherits from integer definition"""

class MyInt(int):
    """modify the positions of int operators == and !=."""

    def __eq__(self, value):
        """Use == opeartor instead of != """
        return self.real != value

    def __ne__(self, value):
        """Use  != operator instead of == """
        return self.real == value
