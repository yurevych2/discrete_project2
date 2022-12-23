from numpy import array, polydiv

def transform_equation(coefs):
    '''
    Divides an equation by r to the lowest power and returns a power equation.
    >>> transform_equation([2, 3, 4])
    ([-1, 2, 3, 4], '-1*r**3 + 2*r**2 + 3*r**1 + 4*r**0')
    '''
    power = len(coefs)
    coefs = [-1] + coefs
    result = []
    for i in coefs:
        result.append(str(i) + '*r**' + str(power - coefs.index(i)))

    return coefs, ' + '.join(result)

def derivative_func(coefs):
    '''
    Finds the derivative of polymonial at the point r = 0.
    list -> int|float
    >>> derivative_func([2, -5, 2])
    -5
    >>> derivative_func([2, 5, 7, 8])
    7
    >>> derivative_func([2, 3, 7, 8, 3])
    8
    >>> derivative_func([9, 2, 3, 1, 0, 0, 6])
    0
    '''
    power = len(coefs)
    der_at_point = coefs[power - 2]
    return der_at_point


def find_interval(equation, coefs):
    '''
    (str, list) -> list|int
    Finds the interval at the ends of
    which the function has different signs. If the function has
    integer point (so that the function = 0 at this point), returns this point.
    >>> find_interval('2*r - 3', [2, -2])
    [0, 2]
    >>> find_interval('r**2 - 2*r + 1', [1, 2, -2, 1])
    1
    '''
    r = 0
    func_at_0 = eval(equation)
    der_at_0 = derivative_func(coefs)
    if func_at_0 == 0:
        return 0
    try:
        if func_at_0 > 0:
            #Than the function is growing at 0:
            if der_at_0 >= 0:
                r = 0
                while eval(equation) > 0:
                    r -= 1
                    if eval(equation) == 0:
                        return r
                start = r
                end = 0
            #Than the funcntion is falling at 0:
            elif der_at_0 < 0:
                r = 0
                while eval(equation) >= 0:
                    r += 1
                    if eval(equation) == 0:
                        return r
                start = 0
                end = r
        elif func_at_0 < 0:
            if der_at_0 >= 0:
                r = 0
                while eval(equation) < 0:
                    r += 1
                    if eval(equation) == 0:
                        return r
                start = 0
                end = r
            elif der_at_0 < 0:
                r = 0
                while eval(equation) < 0:
                    r += 1
                    if eval(equation) == 0:
                        return r
                start = r
                end = 0
        return [start, end]
    except TimeoutError:
        print('Error')

def one_root(equation, interval, epsilon):
    '''
    Returns one root of the polymonial equation.
    '''
    if isinstance(interval, int):
        return interval
    start = interval[0]
    end = interval[1]
    middle = (start + end)/2
    r = middle
    if eval(equation) >= -epsilon and eval(equation) <= epsilon:
        return middle
    if eval(equation) > epsilon:
        end = middle
    elif eval(equation) < -epsilon:
        start = middle
        end = end
    return middle

def division(coefs1, coefs2):
    '''
    (list, list) -> list
    Divide two polinomials.
    >>> division([1, -4, 5, -2], [1, -1])
    [1.0, -3.0, 2.0]
    >>> division([1, 2, 1], [1, 1])
    [1.0, 1.0]
    '''
    lst = []
    x = array(coefs1)
    y = array(coefs2)
    result = polydiv(x, y)[0]
    for i in result:
        if isinstance(i, float):
            lst.append(i)
    return lst

def make_equation(coefs):
    '''
    list -> str
    Makes equation from the list of coefs.
    '''
    power = len(coefs) - 1
    result = []
    for i in coefs:
        if i >= 0:
            result.append('+ ' + str(i) + '*r**' + str(power - coefs.index(i)))
        elif i < 0:
            result.append(str(i) + '*r**' + str(power - coefs.index(i)))
    return ''.join(result)


def get_root(equation, coefs, epsilon):
    '''
    (str, list, float) -> list
    Finds all roots of the polynomial.
    >>> get_root('r- 2', [1, -2], 0.1)
    [2]
    >>> get_root('r**2 - 2*r + 1', [1, -2, 1], 0.1)
    [1, 1]
    >>> get_root('r**2 - 4*r**2 + 3', [1, -4, 3], 0.1)
    [1, 3]
    >>> get_root('r**3 - 4*r**2 + 5*r - 2', [1, -4, 5, -2], 0.1)
    [1, 1, 2]
    '''
    power = len(coefs) - 1
    result = []
    #Finding interval, where function has different signs:
    interval = find_interval(equation, coefs)
    root = one_root(equation, interval, epsilon)
    result.append(root)
    while len(result) < power:
        coefs2 = [1, -root]
        coefs = division(coefs, coefs2)
        equation = make_equation(coefs)
        root = one_root(equation, find_interval(equation, coefs), epsilon)
        result.append(root)
    return result

def coincidence_of_roots(roots):
    '''
    list -> dict
    Returns a dictionary in which the key is the roots,
    and the value is the number of matches of these roots.
    >>> coincidence_of_roots([1, 5, 2, 1])
    {1: 2, 5: 1, 2: 1}
    '''
    counts = dict()
    for item in roots:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts
