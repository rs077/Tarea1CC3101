# Por favor complete con su nombre y RUT.
# NOMBRE Y APELLIDO: Rodrigo Soria
# RUT: 18.358.776-5

# Run the file as "python SAT.py -v"

# Add further needed modules
import unittest

# To implement the functions below, you are allowed
# to define auxiliary functions, if convenient.


def SetLiteral(formula, lit):
    """
    :param formula: lista de listas que codifican una formula proposicional.
    :param lit: entero que representa un literal.
    :return: formula simplificada segun el literal.
    """
    for i in range(len(formula)):
        if lit or -lit in formula[i]: # si literal esta en la formula
            if lit > 0:  # si literal es verdadero.
                if lit in formula[i]: # si literal esta en la clausula, se elimina la clausula.
                    formula.remove(formula[i])
            if lit < 0:  # si literal el falso.
                if lit in formula[i]: # si literal esta en la clausula, se elimina el literal.
                    formula[i].remove(lit)
    return formula

def IsSatisfiable(formula):
    # Define your function here
    pass

def BuildModel(formula):
    # Define your function here
    pass

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
