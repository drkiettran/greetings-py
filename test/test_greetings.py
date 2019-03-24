from src.greetings import *
import unittest


class test_greetings(unittest.TestCase):
    def test_hello(self):
        say = greetings()
        actual = say.hello("Jackie")
        self.assertEqual(actual, "Hello, Jackie from " + socket.gethostname() + "/" + str(os.getpid()))


if __name__ == '__main__':
    unittest.main()