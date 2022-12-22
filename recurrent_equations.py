'''
Modul that solve reccurent equations in two ways: slow and speed.
'''

from copy import deepcopy
from numpy import array, matmul
from numpy.linalg import matrix_power, det

def modify_equation(equation):
    '''
    Raise TypeError if the data type is not str. Replace ' - ' with ' + -'.

    >>> modify_equation('4*a(n-1) + 2*a(n-2) - 6*a(n-3)')
    '4*a(n-1) + 2*a(n-2) + -6*a(n-3)'
    '''
    # verification of input data
    if isinstance(equation, str) == False:
        raise TypeError('Equation must me a string.')

    # equation modification
    if " - " in equation:
        equation = equation.replace(" - ", " + -")
    
    return equation

def general_solution(equation) -> tuple:
    """
    Returns a general solution of recurrent equations and list of coefficients.

    >>> general_solution("4*a(n-1) + 0.25*a(n-2) + -6*a(n-3)")
    ('A1*r^(n-1) + A2*r^(n-2) + A3*r^(n-3)', [4.0, 0.25, -6.0])
    """
    # creating a list of coefficients and transforming the equation
    coeff = []

    # equation modification
    equation = equation.replace("a", "r^")
    a = equation.split(" + ")
    for i in range(len(a)):
        coeff.append(float(a[i].split("*")[0]))
        a[i] = f"A{i+1}*" + a[i].split("*")[-1]
    equation = (" + ").join(a)

    return equation, coeff

def find_roots() -> list[float]:
    '''
    Documentation and docstring.
    Шукає r.
    ТАРАС
    '''

def get_coefs(equation) -> str:
    """
    Fucntion returns roots of equation system using Cramer`s method.
    >>> get_coefs(( "2*A1 + 5*A2 = 19", \
                    "1*A1 + -2*A2 = -4"))
    [2.0, 3.0]
    >>> get_coefs(( "2*A1 + 1*A2 + 3*A3 = 10", \
                    "1*A1 + 1*A2 + 1*A3 = 6", \
                    "1*A1 + 3*A2 + 2*A3 = 13"))
    [2.0, 3.0, 1.0]
    """
    # definition coeff
    coeff = []
    for i in range(len(equation)):
        row  = []
        a = equation[i].split(" + ")
        for j in range(len(a)):
            row.append(int(a[j].split("*")[0]))
        coeff.append(row)

    # definition res   
    res = [int(equation[i].split(" = ")[1]) for i in range(len(equation))]

    def rmatrix(n):
        pro = deepcopy(coeff)
        for e in range(len(coeff)):
            if n != 0:
                pro[e][n-1] = res[e]
        return pro

    # matrix determinant
    det_ = [det(array(rmatrix(n))) for n in range(len(equation)+1)]

    #roots
    final = [round(det_[u]/det_[0],2) for u in range(1, len(equation)+1)]

    return final

def final_solution_one_el(equation, Rs, As) -> float:
    """
    Substitutes r, A and returns the final solution of the nth term.

    >>> final_solution_one_el('A1*r^(n-1) + A2*r^(n-2) + A3*r^(n-3)', [1,2,3], [1,2,3])
    '1*1^(n-1) + 2*2^(n-2) + 3*3^(n-3)'
    """
    if len(Rs) != len(equation.split(' + ')) or len(As)!= len(equation.split(' + ')):
        return 'Kinda cringe bro'

    for el in range(len(As)):
        equation = equation.replace(f'A{el+1}', str(As[el]))

    for xd in range(len(Rs)):
        equation = equation.replace(f'r{xd+1}', str(Rs[xd]))

    return equation

def final_solution_plural_el(nums: list) -> list[float]:
    '''
    arg nums: номера елементів для обрахунку (ті, які треба знайти)
    Documentation and docstring.
    Викликає Н разів final_solution_one_el(), щоб обрахувати елементи з номером
    з переліка, який отримує функція.
    ВІКА
    '''
    pass

def get_transitive_matrix(equation: str):
    '''
    Return transitive matrix to find n-th element of the secuence.

    >>> get_transitive_matrix('3*a(n-1) + 10*a(n-2)')
    [[0, 10.0], [1, 3.0]]
    '''
    matrix_size = equation.count(' + ') + 1
    coefs = general_solution(equation)[-1]
    matrix = [[coef] for coef in coefs[::-1]]
    for row in range(matrix_size):
        for _ in range(matrix_size-1):
            matrix[row].insert(0, 0)

    for row in range(matrix_size+1):
        for column in range(matrix_size+1):
            if row and row == column - 1:
                matrix[row][column-2] = 1

    return matrix

def get_nth_el(equation: str, first_els: list, n: int):
    '''
    Find n-th element of reccurence relationship.
    :param first_els list: values of basic elements. [a(n-1)] for a(n) = 2*a(n-1).
    :param n int: number of element to find. Indexes from 0.

    >>> get_nth_el('3*a(n-1) + 10*a(n-2)', [1, 43], 4)
    847.0
    >>> get_nth_el('3*a(n-1) + 10*a(n-2)', [1, 43], 1)
    43
    '''
    transist_matrix = get_transitive_matrix(equation)
    if n < len(first_els):
        return first_els[n]
    else:
        matrix = matrix_power(array(transist_matrix), n-2)
        n_th = list(matmul(array(first_els), matrix))[-1]
        return n_th

def speed_analisys():
    '''
    Documentation and docstring.
    НАТАЛІ
    '''
    pass
