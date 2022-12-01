# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# *Примеры:*
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
if x*x == y or y*y==x:
    print(f"{x}, {y} -> да")
else:
    print(f"{x}, {y} -> нет")


# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

arr = []
for i in range(5):
    arr.append(int(input(f"Enter a number {i}: ")))
print(f"{arr} -> {max (arr)}")


# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

stop = int(input("Enter a number: "))
start = stop * -1
for i in range(start,stop + 1):
    if i < stop:
        print(f"{i}, ", end='')
    else:
        print(f"{i}")


# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

x = float(input("Enter a number: "))
y = int(round(x%1*10,0))
if y == 0:
    print(f"{x} -> нет")
else:
    print(f"{x} -> {y}")    


# 5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

x = int(input("Enter a number: "))
if (x % 5 == 0 and x % 10 == 0 or x % 15 == 0) and x % 30 != 0:
    print("true")
else:
    print("False")

