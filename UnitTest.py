import unittest
import math
from Project_2 import graphColoring, readFile


class Test(unittest.TestCase):
    def test0(self):
        data = readFile("TestCases\\test0.txt")
        result = graphColoring(data)
        self.assertTrue(result != False)

    def test1(self):
        data = readFile("TestCases\\test1.txt")
        result = graphColoring(data)
        self.assertTrue(result != False)

    def test2(self):
        data = readFile("TestCases\\test2.txt")
        result = graphColoring(data)
        self.assertTrue(result != False)

    def test3(self):
        data = readFile("TestCases\\test3.txt")
        result = graphColoring(data)
        self.assertTrue(result != False)

    def test4(self):
        data = readFile("TestCases\\test4.txt")
        result = graphColoring(data)
        self.assertTrue(result == False)

    def test5(self):
        data = readFile("TestCases\\test5.txt")
        result = graphColoring(data)
        self.assertTrue(result != False)

    def test6(self):
        data = readFile("TestCases\\test6.txt")
        result = graphColoring(data)
        self.assertTrue(result != False)


def unitTest():
    unitTest = unittest.TestSuite()

    # TestSuite represents an aggregation of individual test cases
    for i in range(6):
        name = 'test' + str(i)

        unitTest.addTest(Test(name))

    return unitTest


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(unitTest())
