# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 12. Выбор из нескольких вариантов
 Вход: 
   3
   16
 Результат:
   31
   школьник
"""
m = int(  input("Введите номер месяца: ") )
if m == 2: d = 28    
elif m in [1,3,5,7,8,10,12]: d = 31
else: d = 30

print( "Дней в месяце:", d )
print()
v = int( input("Введите возраст: ") )
if v in range(7): print("дошкольник")    
elif v in range(7,18): print("школьник")    
else:   print("взрослый")
