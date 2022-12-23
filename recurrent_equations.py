'''
Description
'''
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
    solutions_lst = []
    for element in range(num):
        solution = final_solution_one_el(element)
        solutions_lst.append(solution)
    return solutions_lst

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
