"""С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E
заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение, а целенаправленное.

Вариант 12.	Формируется матрица F следующим образом: если в B количество простых чисел в нечетных столбцах в области 2 больше,чем сумма чисел в
четных строках в области 1, то поменять в E симметрично области 1 и 2 местами, иначе С и Е поменять местами несимметрично. При этом матрица А не меняется.
После чего вычисляется выражение: (K*A)*A-K*AT. Выводятся по мере формирования А, F и все матричные операции последовательно.
"""

#                       4
#   D   E           3       1
#   C   B               2

from math import ceil, floor
import random

def printMatrix(matrix): # функция вывода матрицы
   for i in range(len(matrix)):
      for j in range(len(matrix[i])):
          print ("{:5d}".format(matrix[i][j]), end="")
      print()
      
n = int(input('Введите число число N, большее или равное 5: '))
while n < 5:
    n = int(input("Введите число N, большее или равное 5: "))
k = int(input('Введите число число K: '))

# вывод матрицы А(N,N) c диапазоном значений от -10 до 10
A = [ [ random.randint(-10, 10) for j in range(n)] for i in range(n) ]
print('\nМатрица А:')
printMatrix(A)

F = [[elem for elem in raw] for raw in A]         # матрица F, на данный момент равной матрице A
F_dump = [[elem for elem in raw] for raw in F]        # резервная копия матрицы F

submatrix_order = ceil(n/2)  # определение порядка подматрицы

# вычленяем матрицу B через срезы
# проверка n на четность нужна чтобы матрица А делилась на равные 4 подматрицы

if n % 2 == 0:
    b = [F[i][submatrix_order:n] for i in range(0, submatrix_order)]
else:
    b = [F[i][submatrix_order-1:n] for i in range(0, submatrix_order)]

#колличество простых чисел в нечётных столбцах в области 2
list = []
for i in range(submatrix_order):
    for j in range(submatrix_order):
        if (i <= j) and ((i + j + 1) >= submatrix_order) and (j+1) % 2 != 0:
            list.append(b[i][j])
minvalue = min(list)

#сумма чисел в четных строках в области 1
sumvalue = 0
for i in range(submatrix_order):
    for j in range(submatrix_order):
        if (i >= j) and ((i + j + 1) <= submatrix_order) and (i+1) % 2 == 0:
            sumvalue += b[i][j]

#ниже выполнение инструкций по условию
if minvalue > sumvalue:
    print('\nВ B количество простых чисел в нечётных столбцах в области 2 больше чем сумма в чётных строках в, \n'
          'области 1, то меняем в E симметрично области 1 и 2 места\n')
    
    for i in range(submatrix_order, n):
        for j in range(submatrix_order, n):
            if i >= j:
                F_dump[i][j] = F[submatrix_order - j - 1][submatrix_order - i -1]
    print("Матрица F:")
    F = F_dump
    printMatrix(F)
else:
    print('\nВ B количество простых чисел в нечётных столбцах в области 2 меньше или равно чем сумма чисел в чётных строках в , \n'
          'области 1, то меняем в C и Е местами несимметрично\n')
    for i in range(ceil(n/2)):
        for j in range(ceil(n/2), n):
            F[i][j] = F_dump[floor(n / 2) + i][j]
            F[floor(n / 2) + i][j] = F_dump[i][j]
    print("Матрица F:")
    printMatrix(F)


KA = [[0 for i in range(n)] for j in range(n)]           #результат умножения коэффициента К на матрицу A
for i in range(n):      #умножение матрицы на коэффициент
    for j in range(n):
            KA[i][j] = k * A[i][j]
print('\nРезультат умножения коэффициента K на матрицу А:')
printMatrix(KA)

KAA = [[0 for i in range(n)] for j in range(n)]          # умножние матрицы KA на матрицу A
for i in range(n):  # умножения матриц
    for j in range(n):
        for l in range(n):
            KAA[i][j] += KA[j][i] * A[l][j]
print("\nУмножение матрицы KA на матрицу A:")
printMatrix(KAA)

AT = [[0 for i in range(n)] for j in range(n)]           # транспонированная матрица A
for i in range(n):  # произведение транспонирования матрицы A
    for j in range(n):
        AT[i][j] = A[j][i]
print("\nТранспонированная матрица A:")
printMatrix(AT)

KAT = [[0 for i in range(n)] for j in range(n)]
for i in range(n):  # умножение транспонированной матрицы А на коэффициент К
    for j in range(n):
        KAT[i][j] = AT[i][j] * k
print("\nРезультат умножения коэффициента K на матрицу AT:")
printMatrix(KAT)

matrix_result = [[0 for i in range(n)] for j in range(n)]  # заготовка под конечный результат
for i in range(n):              #разность между двух матриц
    for j in range(n):
        matrix_result[i][j] = KAA[i][j] - KAT[i][j]
print("\nКонечный результат KAA - KAT:")
printMatrix(matrix_result)

print("\nРабота программы завершена")
