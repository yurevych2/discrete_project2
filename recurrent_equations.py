'''
Description
'''
def general_solution(equation) -> tuple:
    """
    Returns an general solution of recurrent equations and list of coefficients.
    >>> general_solution("-6*a(n-3) + 0.25*a(n-2) + 4*a(n-1)")
    ('A1*r^(n-1) + A2*r^(n-2) + A3*r^(n-3)', [-6.0, 0.25, 4.0])
    >>> general_solution("1*a(n-4) + 8*a(n-3) + 3*a(n-2) - 10*a(n-1)")
    ('A1*r^(n-1) + A2*r^(n-2) + A3*r^(n-3) + A4*r^(n-4)', [1.0, 8.0, 3.0, 10.0])
    >>> general_solution("-6*a(n-3) + 2*a(n-2) + 4*a(n-1)")
    ('A1*r^(n-1) + A2*r^(n-2) + A3*r^(n-3)', [-6.0, 2.0, 4.0])
    >>> general_solution(3)
    'Incorrect input'
    """
    # verification of input data
    if isinstance(equation, str) == False:
        return "Incorrect input"

    # equation modification
    equation = equation.replace("a", "r^")
    if " - " in equation:
        equation = equation.replace(" - ", " + ")
    
    # creating a list of coefficients and transforming the equation
    coeff = []
    a = equation.split(" + ")
    for i in range(len(a)):
        coeff.append(float(a[i].split("*")[0]))
        a[i] = f"A{len(a)-i}*" + a[i].split("*")[-1]
    equation = (" + ").join(a[::-1])

    return equation, coeff

def find_roots() -> list[float]:
    '''
    Documentation and docstring.
    Шукає r.
    ТАРАС
    '''

def get_coefs() -> str:
    """
    Fucntion returns roots of equation system using Cramer`s method.
    >>> get_coefs((\
        "2*A1 + 5*A2 = 19", \
        "1*A1 + -2*A2 = -4"))
    [2.0, 3.0]
    >>> get_coefs((\
        "2*A1 + 1*A2 + 3*A3 = 10", \
        "1*A1 + 1*A2 + 1*A3 = 6", \
        "1*A1 + 3*A2 + 2*A3 = 13"))
    [2.0, 3.0, 1.0]
    >>> get_coefs((\
        "1*A1 + 2*A2 + 3*A3 + -2*A4 = 6", \
        "3*A1 + 2*A2 + -1*A3 + 2*A4 = 4", \
        "2*A1 + -1*A2 + -2*A3 + -3*A4 = 2", \
        "2*A1 + -3*A2 + 2*A3 + 1*A4 = 8"))
    [2.11, -0.33, 1.44, -0.11]
    """
    import numpy as np
    import copy

    # definition coeff
    coeff = []
    for i in range(len(input)):
        row  = []
        a = input[i].split(" + ")
        for j in range(len(a)):
            row.append(int(a[j].split("*")[0]))
        coeff.append(row)

    # definition res   
    res = [int(input[i].split(" = ")[1]) for i in range(len(input))]

    def rmatrix(n):
        pro = copy.deepcopy(coeff)
        for e in range(len(coeff)):
            if n != 0:
                pro[e][n-1] = res[e]
        return pro

    # matrix determinant
    det = [np.linalg.det(np.array(rmatrix(n))) for n in range(len(input)+1)]

    #roots
    final = [round(det[u]/det[0],2) for u in range(1, len(input)+1)]

    return final

def final_solution_one_el() -> float:
    '''
    Documentation and docstring.
    Підставляє r, А в загальне рівняння А_н. Повертає фінальний розв'язок А_н.
    МАРТА
    >>> final_solution_one_el()
    '''
    equation = analytic_solution()
    Rs = find_roots()
    As = get_coefs()
    #r = [829482394823,2,9839283,4]
    #As = [56,2,3,4]
    #equation = 'A1*r1^(n-1) + A2*r2^(n-2) + A3*r3^(n-3) + A4*r4^(n-4)'

    if len(Rs) != len(equation.split(' + ')) or len(As)!= len(equation.split(' + ')):
        return 'Kinda cringe bro'

    for el in range(len(As)):
        equation = equation.replace(f'A{el+1}',str(As[el]))

    for xd in range(len(Rs)):
        equation = equation.replace(f'r{xd+1}',str(Rs[xd]))

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

def exact_element() -> float:
    '''
    Documentation and docstring.
    НАТАЛІ
    '''
    pass

def speed_analisys():
    '''
    Documentation and docstring.
    НАТАЛІ
    '''
    pass
