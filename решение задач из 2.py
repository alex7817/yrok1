#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# for i in range(1,6,1):
#     print(i,"00000")
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# number = int(input("введите цифру "))
# digits_numbar = 5
# count = 0
# for i in range(10):
#     number = int(input("введите цифру "))
#     if number == 5:
#         count+=1
# print(count)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# mult = 1
#
# for i in range(1,11):
#     mult*=i
# print(mult)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# integer_number = 9785345
#
# print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
# sum = 0
# number = int(input("введите цифру "))
# while number > 0:
#     if number%10!=0:
#         sum+=number%10
#     number=number//10
# print(sum)

'''
Задача 7
Найти произведение цифр числа.
'''
# mult = 1
# number = int(input("введите цифру "))
# while number > 0:
#     if number%10!=0:
#         mult*=number%10
#     number=number//10
# print(mult)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 2134135
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
# number = int(input("введите цифру "))
# max_digit=0
# while number>0:
#     if number%10>max_digit:
#         max_digit=number%10
#     number=number//10
# print(max_digit)
'''
Задача 10
Найти количество цифр 5 в числе
'''
# number = int(input("введите цифру "))
# digits_numbar = int(input("что ищем"))
# count = 0
# while number>0:
#  if number%10 == digits_numbar:
#     count += 1
#  number=number//10
# print(count)

