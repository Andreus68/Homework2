# Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.
# Пример:  пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

import random
arrstart = []
arr = []
number = int(input('Введите число '))

for i in range(number):
   j = random.randint(-10,10)
   arrstart.append(j)
   arr.append(j)
   if j < 0: arr.append(0)
print(arrstart)
print(arr)





