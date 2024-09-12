# Задайте переменные разных типов данных:
# Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
# Выполните операции вывода кортежа immutable_var на экран.

immutable_var = "Mercedes", 600, 6.0, True # Использовано 4 типа данных: str, int, float, bool
print (immutable_var, type(immutable_var))

# Изменение значений переменных:
# Попытайтесь изменить элементы кортежа immutable_var.
# Объясните, почему нельзя изменить значения элементов кортежа.

#immutable_var [0] = 200 # Выдаст ошибку, кортеж не поддерживает обращение по элементам.


#Создание изменяемых структур данных:
#Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
# Измените элементы списка mutable_list.
# Выведите на экран измененный список mutable_list.


# Варинат №1 изменения элемента списка
mutable_list = (["Espresso","Cappuccino"],"Latte")
print (mutable_list, type(mutable_list))
mutable_list [0][0] = "Raf"
print (mutable_list, type(mutable_list))


# Варинат №2 изменения элемента списка
mutable_list = ["Espresso", "Cappuccino", "Latte"]
print (mutable_list, type(mutable_list))
mutable_list [0] = "Raf"
mutable_list [1] = "Ice Cappuccino"
mutable_list [2] = "Ice Latte"
print (mutable_list, type(mutable_list))