import random
import itertools as it
from SampleOO.Person import *;

class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum

    def Test(self):
        super(Employee, self).Test()
        print("Employee3: =>" + self.Name() + ", " +  str(self.staffnumber) )

