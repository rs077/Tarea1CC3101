# Por favor complete con su nombre y RUT.
# NOMBRE Y APELLIDO: Rodrigo Soria
# RUT: 18.358.776-5

# Run the file as "python SAT.py -v"

# Add further needed modules
import unittest
import random
# To implement the functions below, you are allowed
# to define auxiliary functions, if convenient.


def SetLiteral(formula, lit):
    """
    funcion que simplifica una formula segun un literal dado.
    :param formula: lista de listas que codifican una formula proposicional.
    :param lit: entero que representa un literal.
    :return: formula simplificada segun el literal.
    """
    for i in range(len(formula)):
        if lit or -lit in formula[i]:  # si literal esta en la formula
            if lit > 0:  # si literal es verdadero.
                if lit in formula[i]:  # si literal esta en la clausula, se elimina la clausula.
                    formula.remove(formula[i])
            if lit < 0:  # si literal el falso.
                if lit in formula[i]:  # si literal esta en la clausula, se elimina el literal.
                    formula[i].remove(lit)
    return formula


def IsSatisfiable(formula):
    """
    funcion que determina si una formula es satisfactible.
    :param formula: se determinara si es satisfactible .
    :return: True si es satisfactible, False si no.
    """
    for k in range(len(formula)):  # se iterara sobre las clausulas.
        if len(formula[k]) == 0:  # si hay una clausula con largo cero.
            return False  # formula sera insatisfactible.
    i = random.randint(0, len(formula))  # se elige un indice i arbitrario.
    j = formula[i][random.randint(0, len(formula[i]))]  # se elige un indice j arbitrario.
    literal = formula[i][j]  # se elige un literal arbitrario.
    literal = abs(literal)  # se setea el literal a True.
    formulaSimplificada = SetLiteral(formula, literal)  # se obtiene la formula simplificada.
    if len(formulaSimplificada) == 0:  # se chequea si la formula es satisfactible.
        return True  # formula es satisfactible.
    else:
        literal = literal*-1  # se setea el literal a False.
        formulaSimplificada = SetLiteral(formula, literal)  # se obtiene la formula simplificada.
        if len(formulaSimplificada) == 0:  # se chequea si la formula es satisfactible.
            return True  # formula es satisfactible.
    IsSatisfiable(formulaSimplificada)  # se usa recursividad.


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
        self.assertEqual(IsSatisfiable([[1, 2], [1, -2], [], [-1]]), False)
        self.assertEqual(IsSatisfiable([]), True)

    def test_BuildModel(self):
        self.assertEqual(BuildModel([[-2, 4], [1], [-4,-1]]), (True, {1: True, 2: False, 4: False}))
        self.assertEqual(BuildModel([[1, 2], [-1, -2], [-1, 2], [1, -2]]), (False, {}))

# Perform the tests when runing the file
if __name__ == '__main__':
    unittest.main()
