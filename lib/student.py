#!/usr/bin/env python

from user import User  # Assuming User class is defined in user.py


class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, new_knowledge):
        self.knowledge.append(new_knowledge)
