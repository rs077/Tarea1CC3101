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
    i = len(formula)  # contador que tiene el largo de la formula.
    while i >= 0:  # bucle para recorrer la formula.
        i -= 1
        if i >= 0:  # si el contador es positivo
            if lit in formula[i]:  # si literal esta en la formula.
                formula.remove(formula[i])  # si literal esta en la clausula, se elimina la clausula.
                i-=1  # se reduce el indice ya que se redujo la formula al perder una clausula.
        if i >= 0:  # si el contador es positivo
            if -lit in formula[i]:  # si la negacion del literal esta en la formula.
                formula[i].remove(-lit)  # si literal esta en la clausula, se elimina el literal.
    return formula  # se retorna la formula.


def IsSatisfiable(formula):
    """
    funcion que determina si una formula es satisfactible.
    :param formula: se determinara si es satisfactible .
    :return: True si es satisfactible, False si no.
    """
    largoFormula = len(formula)
    if largoFormula == 0:  # si el largo de la formula es cero, la formula es satisfactible.
        return True
    if largoFormula > 0:  # si la formula tiene largo mayor a cero.
        for i in range(largoFormula):  # se recorre la formula para revisar sus clausulas.
            if len(formula[i]) == 0:  # si hay una clausula con largo cero la formula no es satisfactible.
                return False
    i = random.randint(0, largoFormula - 1)  # se elige un indice i arbitrario.
    j = 0  # se elige un indice j arbitrario, en este caso sera siempre el primero de la clausula.
    literal = formula[i][j]  # se elige un literal arbitrario.
    formulaAux = copy.copy(formula)  # se copia la formula.
    SetLiteral(formula, literal)  # se setea el literal a true y se simplifica la formula.
    if IsSatisfiable(formula):  # si es safisfactible con el literal seteado en True.
        return True
    literal = -literal  # se cambia el signo al literal.
    SetLiteral(formulaAux, literal)  # se setea el literal a false y se simplifica la formula.
    if IsSatisfiable(formulaAux):  # si es safisfactible con el literal seteado en False.
        return True
    return  # se retorna


def BuildModel(formula):
    valuacion = {}  # diccionario donde se almacenara la valuacion.
    formulaAux = copy.copy(formula)  # se copia la formula.
    if IsSatisfiable(formula):  # si la formula es satisfactible se procede.
        largoFormula = 1  # valor default para entrar al bucle a continuacion.
        while largoFormula > 0:  # se revisa el largo de la formula.
            largoFormula = len(formulaAux)  # se extra el largo de la formula.
            if largoFormula == 0:  # si el largo de la formula es cero, la formula es satisfactible.
                break
            for i in range(largoFormula):
                if len(formulaAux[i]) == 0:  # si hay una clausula con largo cero.
                    break
            i = random.randint(0, largoFormula - 1)  # se elige un indice i arbitrario.
            j = 0  # se elige un indice j arbitrario, en este caso sera siempre el primero de la clausula.
            literal = formulaAux[i][j]  # se elige un literal arbitrario.
            valuacion[literal] = True
            SetLiteral(formulaAux, literal)  # se setea el literal a true y se simplifica la formula.
        checkValuacion(valuacion)  # se revisa la valuacion para que tenga sus literales positivos.
        par = (True, valuacion)  # se prepara valuacion en el formato pedido
    else:
        par = (False, valuacion)  # se prepara valuacion en el formato pedido
    return par  # se retorna el par

def checkValuacion(valuacion):
    """
    funcion que revisa si la valuacion tiene valores negativos, cambiando su signo y su valor de verdad por
    el opuestio segun lo solicitado en la tarea.
    :param valuacion:
    :return:
    """
    for valor in valuacion:  # se recorre la valuacion.
        if valor < 0:
            valorPositivo = abs(valor)  # se cambia el signo del literal.
            del valuacion[valor]  # se elimina el literal anterior.
            valuacion[valorPositivo] = False  # se almacena el literal negado.

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
