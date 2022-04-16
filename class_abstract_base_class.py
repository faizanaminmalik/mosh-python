# Abstract base class is a half-baked cookie
# We need to make sure all sub classes from straem have a standard method read() no deviations
# We eill make STraem class as Abstract base class to achieve a standardization
# Also no one is allowed to create object from Straem class directly as it doesnt make sense

from abc import ABC, abstractmethod
class StreamOpenError(Exception):
    pass

class Stream(ABC): # To make it abs base class, derive from ABC
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise StreamOpenError ("Stream alrady open")
        print("Opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise StreamOpenError ("Stream alrady closed")
        print("Closed")
        self.opened = False

    @abstractmethod    # to make abstract method
    def read(self):
        pass

class FileStream(Stream):
   def read(self):
       print ("reading from file")

class NetworkStream(Stream):
    def read(self):
        print ("reading from network")

#When a class has an abstract method, its considered to be an abstract class and we can't instantiate that
#st = Stream()
#st.open()
#st.close()

file1 = FileStream()
file1.open()
file1.read()
file1.close()
