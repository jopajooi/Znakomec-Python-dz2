# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
#  Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
#  Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
import random
x = random.randint(1,1000)

y = random.randint(1,1000)
s= x+y
print("Сумма двух чисел, которых загадал Петя")
print(s)
p= x*y
print("Произведение двух чисел, которых загадал Петя")
print(p)
print(f"Это числа {x} и {y}")
