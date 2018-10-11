# Por favor complete con su nombre y RUT.
# NOMBRE Y APELLIDO: Rodrigo Soria
# RUT: 18.358.776-5

# Run the file as "python SAT.py -v"

# Add further needed modules
import unittest
import random
import copy
# To implement the functions below, you are allowed
# to define auxiliary functions, if convenient.


def SetLiteral(formula, lit):
    """
    funcion que simplifica una formula segun un literal al cual se le asignara un valor true.
    :param formula: lista de listas que codifican una formula proposicional.
    :param lit: entero que representa un literal.
    :return: formula simplificada segun el literal.
    """
    i = len(formula)
    while i >= 0:
        i -= 1
        if i >= 0:
            if lit in formula[i]:  # si literal esta en la formula.
                formula.remove(formula[i])  # si literal esta en la clausula, se elimina la clausula.
                i-=1
        if i >= 0:
            if -lit in formula[i]:  # si la negacion del literal esta en la formula.
                formula[i].remove(-lit)  # si literal esta en la clausula, se elimina el literal.
    return formula


def IsSatisfiable(formula):
    """
    funcion que determina si una formula es satisfactible.
    :param formula: se determinara si es satisfactible .
    :return: True si es satisfactible, False si no.
    """
    largoFormula = len(formula)
    if largoFormula == 0:
        return True
    if largoFormula > 0:
        for i in range(largoFormula):
            if len(formula[i]) == 0:  # si hay una clausula con largo cero.
                return False
    i = random.randint(0, largoFormula - 1)  # se elige un indice i arbitrario.
    largoClausula = len(formula[i])
    j = random.randint(0, largoClausula - 1)  # se elige un indice j arbitrario.
    literal = formula[i][j]  # se elige un literal arbitrario.
    formulaAux = copy.copy(formula)  # se copia la formula
    SetLiteral(formula, literal)  # se setea el literal a true y se simplifica la formula
    if IsSatisfiable(formula):  # si es safisfactible
        return True
    SetLiteral(formulaAux, -literal)
    if IsSatisfiable(formulaAux):
        return True
    return


def BuildModel(formula):
    par = {}
    valuacion = {}
    formulaAux = copy.copy(formula)  # se copia la formula
    if IsSatisfiable(formula):
        largoFormula = 1
        while largoFormula>0:
            largoFormula = len(formulaAux)
            if largoFormula == 0:
                break
            for i in range(largoFormula):
                if len(formulaAux[i]) == 0:  # si hay una clausula con largo cero.
                    break
            i = random.randint(0, largoFormula - 1)  # se elige un indice i arbitrario.
            largoClausula = len(formulaAux[i])
            if largoClausula > 0:
                j = random.randint(0, largoClausula - 1)  # se elige un indice j arbitrario.
            else:
                break
            literal = formulaAux[i][j]  # se elige un literal arbitrario.
            if literal > 0:  # si el literal es True.
                valuacion[literal] = True
                SetLiteral(formulaAux, literal)  # se setea el literal a true y se simplifica la formula
            else:  # si el literal es False.
                valuacion[literal] = False
                SetLiteral(formulaAux, literal)  # se setea el literal a true y se simplifica la formula
        par[True] = valuacion
    else:
        par[False] = valuacion
    return par

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
