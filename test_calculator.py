"""
Unit tests for the calculator library
"""
#We add all the files in the app directory so that they can be found
#from sys import path
#path.append('..\\EASYCHESS')

from app.views import calculator
 
#print(calculator.add(2, 2))

class TestCalculator:

    def test_addition(self):
        print("Testing addition")
        assert 4 == calculator.add(2, 2)
        print("Addition successful")

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    




if __name__ == "__main__":
    print("SUCCESSFULLY DONE")
