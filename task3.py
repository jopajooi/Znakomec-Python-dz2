# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
import sys
sys.set_int_max_str_digits(999999999)
N =int(input("Введите число:  "))

i=0
d=1
o=2
while i<N:
    
    i+=1
    p = o*d
    d=p
    print({p}) 