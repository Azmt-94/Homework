first  = int (input('Введите первое число: '))
second = int (input('Введите второе число: '))
third  = int (input('Введите третье число: '))
if first == second and first == third:
    print ('3') #Если все числа равны между собой, то вывести 3
elif first == second or second == third or first == third:
    print ('2') #Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
else:
    print ('0') #Если равных чисел среди 3-х вообще нет, то вывести 0