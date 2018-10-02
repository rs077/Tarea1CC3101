# Por favor complete con su nombre y RUT.
# NOMBRE Y APELLIDO: Rodrigo Soria
# RUT: 18.358.776-5

# Run the file as "python SAT.py -v"

# Add further needed modules
import unittest

# To implement the functions below, you are allowed
# to define auxiliary functions, if convenient.


def SetLiteral(formula, lit):
    # Define your function here


def IsSatisfiable(formula):
    # Define your function here


def BuildModel(formula):
    # Define your function here


class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_SetLiteral(self):
        self.assertEqual(SetLiteral([[1, 2, -3], [-1, -2, 4], [3, 4]], 1), [[-2, 4], [3, 4]])
        self.assertEqual(SetLiteral([[1, 2, -3], [-1, -2, 4], [3, 4]], -1), [[2, -3], [3, 4]])

    def test_IsSatisfiable(self):
        self.assertEqual(IsSatisfiable([[1, 2, -3], [-1, -2, 4], [3, 4]]), True)
        self.assertEqual(IsSatisfiable([[1, 2], [1, -2], [], [-1]), False)
        self.assertEqual(IsSatisfiable([]), True)

    def test_BuildModel(self):
        self.assertEqual(BuildModel([[-2, 4], [1], [-4,-1]]), (True, {1: True, 2: False, 4: False}))
        self.assertEqual(BuildModel([[1,2], [-1,-2], [-1,2], [1,-2]]), (False, {}))

# Perform the tests when runing the file
if __name__ == '__main__':
    unittest.main()
