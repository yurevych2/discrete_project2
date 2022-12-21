'''
Description
'''
import numpy as np

def general_solution() -> str:
    '''
    Documentation and docstring.
    Загальний розв'язок.
    МАРІЯ
    '''
    pass

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
