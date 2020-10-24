import random as rdm
import array

# Создаем масив с произвольными значениями
n = rdm.randint(1, 100)
a = array.array('b', rdm.sample(range(100), n))

# Создаем подпоследовательность с путем среза начала и конца массива а
x = len(a)//2
b = rdm.randint(0, x)
v = rdm.randint(x, len(a))
c = a[b:v]
m = len(c)

print(sum(c))
