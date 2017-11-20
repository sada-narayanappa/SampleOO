import random

class Person:
    personTest=0;
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    @staticmethod
    def staticMethodWithDecor(arg=None):
        print (arg+ " Static Method: staticMethodWithDecor")

    def staticMethodNoDecor(arg=None):
        print (arg+ " Static Method: staticMethodNoDecor")

    @classmethod
    def classMethodWithDecor(arg=""):
        print (str(arg)+ " Class Method: classMethodWithDecor")

    def Name(self):
        return "Person11: " + self.firstname + " " + self.lastname

    def Test(self):
        Person.personTest += 1
        print (self.Name() + " " + str(Person.personTest))

