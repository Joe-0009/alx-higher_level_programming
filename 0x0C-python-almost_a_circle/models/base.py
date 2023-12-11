#!/usr/bin/python3
""" Module that contains class Base """
import json
import csv
import turtle


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes instances """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        if list_objs is None:
            list_objs = []

            filename = f"{cls.__name__}.json"
            with open(filename, 'w') as file:
            json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_str)

     @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

     @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy_instance = cls(1, 1)
            else:
                new = cls(1)
            dummy_instance.update(**dictionary)
            return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
         filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r') as file:
                data = file.read()
                if not data:
                    return []

                json_data = cls.from_json_string(data)
                return [cls.create(**obj_dict) for obj_dict in json_data]

        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = f"{cls.__name__}.csv"

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = f"{cls.__name__}.csv"

        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                instances = []

                for row in reader:
                    if cls.__name__ == "Rectangle" and len(row) == 5:
                        instances.append(cls.create(id=int(row[0]), width=int(row[1]), height=int(row[2]), x=int(row[3]), y=int(row[4])))
                    elif cls.__name__ == "Square" and len(row) == 4:
                        instances.append(cls.create(id=int(row[0]), size=int(row[1]), x=int(row[2]), y=int(row[3])))

                return instances

        except FileNotFoundError:
            return []
