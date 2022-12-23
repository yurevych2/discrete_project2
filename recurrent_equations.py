'''
Modul that solve reccurent equations in two ways: slow and speed.
Also you can get analysis of work of functions.
'''

from copy import deepcopy
from numpy import array, matmul
from numpy.linalg import matrix_power, det

def modify_equation(equation_: str) -> str:
    '''
    Raise TypeError if the data type is not str. Replace ' - ' with ' + -'.

    >>> modify_equation('4*a(n-1) + 2*a(n-2) - 6*a(n-3)')
    '4*a(n-1) + 2*a(n-2) + -6*a(n-3)'
    '''
    equation = deepcopy(equation_)

    # verification of input data
    if isinstance(equation, str) == False:
        raise TypeError('Equation must me a string.')

    # equation modification
    if ' - ' in equation:
        equation = equation.replace(' - ', ' + -')
    
    return equation

def general_solution(equation_: str) -> tuple:
    '''
    Returns a general solution of recurrent equations and list of coefficients.

    >>> general_solution('4*a(n-1) + 0.25*a(n-2) + -6*a(n-3)')
    ('A1*r^(n-1) + A2*r^(n-2) + A3*r^(n-3)', [4.0, 0.25, -6.0])
    '''
    equation = deepcopy(equation_)

    # creating a list of coefficients and transforming the equation
    coeff = []

    # equation modification
    equation = equation.replace('a', 'r^')
    a = equation.split(' + ')
    for i in range(len(a)):
        coeff.append(float(a[i].split('*')[0]))
        a[i] = f'A{i+1}*' + a[i].split('*')[-1]
    equation = (' + ').join(a)

    return equation, coeff

def find_roots() -> list[float]:
    '''
    Documentation and docstring.
    Шукає r.
    ТАРАС
    '''

def replace_r(equation_: str, roots: list):
    '''
    Replace r with its value.

    >>> replace_r('A1*r^(n-1) + A2*r^(n-2) + A3*r^(n-3)', [1, 3, 5])
    'A1*1**n + A2*3**n + A3*5**n'
    '''
    equation = deepcopy(equation_)
    
    i = 0
    while i < len(roots):
        equation = equation.replace(f'r^(n-{i+1})', f'{roots[i]}**n')
        i += 1
    
    return equation

def get_system(equation_: str, base: list[int]):
    '''
    :param base list[int]: basic elements the n-th element depends on it.

    >>> get_system('A1*1**n + A2*3**n + A3*5**n', [3, 5])
    ('1*A1 + 3*A2 + 5*A3 = 3', '1*A1 + 9*A2 + 25*A3 = 5')
    '''
    equation = deepcopy(equation_)

    result = []
    for index, num in enumerate(base):
        equation_ = deepcopy(equation)
        equation_ = equation_.replace('n', str(index + 1))
        equation_ = equation_.split(' + ')

        powered_equation = []
        for part in equation_:
            index = part.find('*')
            number = eval(part[index+1:])
            powered_equation.append(f'{number}*{part[:index]}')

        equation_ = ' + '.join(powered_equation) + f' = {num}'
        result.append(equation_)
    
    return tuple(result)

def get_coefs(equation_: str) -> str:
    '''
    Fucntion returns roots of equation system using Cramer`s method.
    >>> get_coefs(( '2*A1 + 5*A2 = 19', \
                    '1*A1 + -2*A2 = -4'))
    [2.0, 3.0]
    >>> get_coefs(( '2*A1 + 1*A2 + 3*A3 = 10', \
                    '1*A1 + 1*A2 + 1*A3 = 6', \
                    '1*A1 + 3*A2 + 2*A3 = 13'))
    [2.0, 3.0, 1.0]
    '''
    # definition coeff
    coeff = []
    for i in range(len(equation_)):
        row  = []
        a = equation_[i].split(' + ')
        for j in range(len(a)):
            row.append(int(a[j].split('*')[0]))
        coeff.append(row)

    # definition res   
    res = [int(equation_[i].split(' = ')[1]) for i in range(len(equation_))]

    def rmatrix(n):
        pro = deepcopy(coeff)
        for e in range(len(coeff)):
            if n != 0:
                pro[e][n-1] = res[e]
        return pro

    # matrix determinant
    det_ = [det(array(rmatrix(n))) for n in range(len(equation_)+1)]

    #roots
    final = [round(det_[u]/det_[0],2) for u in range(1, len(equation_)+1)]

    return final

def final_solution_one_el(equation_, As) -> float:
    '''
    Substitutes r, A and returns the final solution of the nth term.

    >>> final_solution_one_el('A1*1^(n-1) + A2*2^(n-2) + A3*3^(n-3)', [1,2,3])
    '1*1^n + 2*2^n + 3*3^n'
    '''
    equation = deepcopy(equation_)

    # n-number replaced with n
    for el in range(len(As)):
        equation = equation.replace(f'A{el+1}', str(As[el]))
    
    for i in range(0,len(equation.split())):
        equation = equation.replace(f'(n-{i})','n')

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

def get_transitive_matrix(equation_: str):
    '''
    Return transitive matrix to find n-th element of the secuence.

    >>> get_transitive_matrix('3*a(n-1) + 10*a(n-2)')
    [[0, 10.0], [1, 3.0]]
    '''
    matrix_size = equation_.count(' + ') + 1
    coefs = general_solution(equation_)[-1]
    matrix = [[coef] for coef in coefs[::-1]]
    for row in range(matrix_size):
        for _ in range(matrix_size-1):
            matrix[row].insert(0, 0)

    for row in range(matrix_size+1):
        for column in range(matrix_size+1):
            if row and row == column - 1:
                matrix[row][column-2] = 1

    return matrix

def get_nth_el(equation_: str, first_els: list, n: int):
    '''
    Find n-th element of reccurence relationship.
    :param first_els list: values of basic elements. [a(n-1)] for a(n) = 2*a(n-1).
    :param n int: number of element to find. Indexes from 0.

    >>> get_nth_el('3*a(n-1) + 10*a(n-2)', [1, 43], 4)
    847.0
    >>> get_nth_el('3*a(n-1) + 10*a(n-2)', [1, 43], 1)
    43
    '''
    transist_matrix = get_transitive_matrix(equation_)
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

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
