#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        """
        Initialize a new Dog instance.

        :param name: The dog's name.
        :param breed: The dog's breed; defaults to "Mutt" if not provided.
        """
        self.name = name
        self.breed = breed
