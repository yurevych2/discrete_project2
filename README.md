# Компʼютерний проект
## на тему: Аналіз рекурентних рівнянь

Під час роботи над даним проектом ми розробили ? функцій для реалізації завдання. Ми використостовували наші знання з дискретної математики, інтернет ресурси, щоб знайти найоптимальніший та найефективніший спосіб розвяʼзку та командну роботу.


**modify_equation**

Функція заміняє ' - ' на ' + -' для зручнішої подальшої роботи.
 > modify_equation('4*a(n-1) + 2*a(n-2) - 6*a(n-3)')
 
'4*a(n-1) + 2*a(n-2) + -6*a(n-3)'


**general_solution**

Функція виконує перетворення рівняння, щоб надати йому вигляду загального розвʼязку та зробити зручним для подальших перетворень. Тобто, відбувається утворення характеристичного рівняння. Спершу ми робимо заміну “a” на “r^”. Згодом утворюємо список коефіцієнтів та змінюємо їх у рівнянні на невизначені  A1, A2 і тд. Функція повертає модифіковане рівняння та список коефіцієнтів.

> general_solution('4*a(n-1) + 0.25*a(n-2) + -6*a(n-3)')

('A1*r^(n-1) + A2*r^(n-2) + A3*r^(n-3)', [4.0, 0.25, -6.0])

*Блок про пошук коренів*

**transform_equation**

Приймає коефіцієнти початкового рівняння, без урахування коефіцієнта при старшому степені. Виконує ділення рівняння на r у найбільшому степені, та повертає характеристичне рівняння у вигляді степеневого.

> transform_equation([2, 3, 4])

([-1, 2, 3, 4], '-1*r**3 + 2*r**2 + 3*r**1 + 4*r**0')

**derivative_func**

Приймає список з коефіцієнтами характеристичного р-ня та повертає значення похідної в точці r = 0 (воно нам трішки пізніше буде потрібне).

> derivative_func([2, -5, 2])

-5

**find_interval**

Приймає рівнняння + список коефіцієнтів, повертає проміжок, на кінцях якого функція (рівняння) приймає значення різних знаків. 
Як вона працює:
Першою точкою беремо r = 0, дивимося значення функції в нулі. Потім в залежності від того, чи воно додатнє/від’ємне і чи похідна (додатня чи від’ємна) в цій точці, рухаємося далі з кроком 1 та знаходимо другу точку, яка матиме протилежний знак. Якщо протягом ітерації натикаємося на точку, де значення функції = 0, то просто повертаємо її.

> find_interval('2*r - 3', [2, -2])

[0, 2]

**one_root**

Приймає рівняння, інтервал (з ф-ції find_interval) та точність. Методом бінарного пошуку шукає корінь рівняння та повертає його. 

**division**

Приймає коефіцієнти двох многочленів та ділить їх між собою.

> division([1, -4, 5, -2], [1, -1])

[1.0, -3.0, 2.0]

**make_equation**

Приймає список коефіцієнтів та повертає стрічку з рівнянням.

**get_root**

> get_root('r- 2', [1, -2], 0.1)

[2]

**coincidence_of_roots**

> coincidence_of_roots([1, 5, 2, 1])

{1: 2, 5: 1, 2: 1}

**replace_r**

Функція форматує рівняння для зручної подальшої роботи. Підставляє корені та заміняє знак ‘^’ на ‘**’

> replace_r('A1*r^(n-1) + A2*r^(n-2) + A3*r^(n-3)', [1, 3, 5])

'A1*1**n + A2*3**n + A3*5**n'


**get_system**

Приймає рівняння та перші елементи, від яких залежить значення н-го члена.

> get_system('A1*1**n + A2*3**n + A3*5**n', [3, 5])

('A1*1 + A2*3 + A3*5 = 3', 'A1*1 + A2*9 + A3*25 = 5')


**get_coefs**

Функція рахує систему лінійних рівнянь методом Крамера. Спершу ми створюємо матрицю з коефіцієнтами усіх рівнянь та рядок з результатами рівнянь. Згодом відповідно до алгоритму створюємо матриці та рахуємо їх визначники. При ділені відповідних визначників отримуємо корені рівнянь. Повертає список коренів системи.

> get_coefs(( '2*A1 + 5*A2 = 19', \
                    '1*A1 + -2*A2 = -4'))
[2.0, 3.0]


**final_solution_one_el**
?????

> final_solution_one_el('A1*1^(n-1) + A2*2^(n-2) + A3*3^(n-3)', [1,2,3])

'1*1^n + 2*2^n + 3*3^n'

**final_solution_plural_el**

Функція отримує 1)рівняння виду '1*1^n + 2*2^n + 3*3^n', 2)номер елемента, до якого потрібно проводити пошук, 3)список з початковими елементами, що нам уже задані. Функція повертає список з обрахованих елементів.


**get_transitive_matrix**

Функція повертає транзитивну матрицю для знаходження н-го члена послідовності без пошуку попередніх, що відбувається у функції get_nth_el.

> get_transitive_matrix('3*a(n-1) + 10*a(n-2)')

[[0, 10.0], [1, 3.0]]


**get_nth_el**

Функція обраховує н-ий член послідовності за наступною формулою:
(a0, a1, …) * М^(n-1) = (...., an), де (a0, a1, …)  - члени послідовності від яких залежить значення н-го члена, М - транзитивна матриця.

> get_nth_el('3*a(n-1) + 10*a(n-2)', [1, 43], 1)

43


**speed_analisys**

Функція порівнює результати роботи функції, яка знаходить н-ий член послідовності за O(logN) та інших.


## Висновок:
Ми навчились реалізовувати розвʼязрок рекурентних рівнянь та порівнювати їх швидкість.