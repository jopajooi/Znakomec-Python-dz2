# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
#  Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
#  вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
import random
print("Всего монет")

n=int(input("Введите число n:  "))

k = random.randint(1,n)
print("Монеты, которые лежат решкой вверх")
print(k)
i=0
k1 = n-k
print("Монеты, которые лежат гербом вверх")
print(k1)
if k<k1 or k1==n:
    i=k1+k
    print("Все монеты лежат гербом вверх")
    print(i)
elif k>k1 or k==n:
    i=k1+k
    print("Все монеты лежат решкой вверх")
    print(i)
