#!/usr/bin/python3

"""The base model class definition"""
import json
import csv
import turtle

class Base:
    """Base model classe

    The Class Attributes are:
        __nb_object: the private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """A new Base initialization

        Args:
            id : The public instance attribute identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """the function return the JSON serialization of a list of dictioneries

        Args:
            list_dictionaries : A list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """the functionto  write the JSON serialization of a list of objects to a file

        Args:
            list_objs : list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    def from_json_string(json_string):
        """the function to return the deserialization of a JSON string

        Args:
            json_string (str): A JSON str representation of a list of dictionaries.
        Returns:
            If json_string None or empty, return the string: "[]"
            Otherwise, return the JSON string representation of list_dictionaries otherwise
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    def create(cls, **dictionary):
        """the function returns a class instantied from a dictionary of attributes

        Args:
            **dictionary : Key or value of the attributes to initialize
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    def load_from_file(cls):
        """the function to return a list of instances

        the file is `<cls.__name__>.json`
        the function returns an empty list if the file doen't exist
        or a list of instantiated classes otherwise
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    def save_to_file_csv(cls, list_objs):
        """the function to write the CSV serialization of a list of objects

        Args:
            list_objs : list of instances who inherits of Base
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    def load_from_file_csv(cls):
        """The function that serializes and deserializes in CSV
        the file to read from is `<cls.__name__>.csv`.
        The return is: an empty list if the file doen't exist
        Or a list of instantiated classes Otherwise
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    def draw(list_rectangles, list_squares):
        """The function opens a window and draws all the Rectangles and Squares
        Args:
            list_rectangles (list): the drawn  rectangle objects
            list_squares (list): the drawn list of Square objects
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
