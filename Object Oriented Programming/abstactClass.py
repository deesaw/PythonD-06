#this is a class which cannot be instantiated


#Can only be inherited from
from abc import ABCMeta,abstractmethod

class BaseClass(object):
    __metaclass__=ABCMeta

    @abstractmethod
    def printHam(self):
        pass
class InClass(BaseClass):
    def printHam(self):
        print "ham"

#x=BaseClass() #cannot instantiate

x=InClass()
x.printHam()
    
