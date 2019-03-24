import socket
import os

class greetings:
    def __init__(self):
        """Constructor for this class..."""
        print("Creating object : " + self.__class__.__name__)
        
    def hello(self, name):
        return "Hello, " + name + " from " + socket.gethostname() + "/" + str(os.getpid())
