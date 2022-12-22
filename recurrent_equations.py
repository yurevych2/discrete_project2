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
    '''
    Documentation and docstring.
    Шукає коефіцієнти. Тут система рівнянь.
    МАРТА
    '''
    pass

def final_solution_one_el() -> float:
    '''
    Documentation and docstring.
    Підставляє r, А в загальне рівняння А_н. Повертає фінальний розв'язок А_н.
    МАРТА
    '''
    pass

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
