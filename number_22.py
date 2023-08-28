# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def GetInt(str):
    n = int(input(f"Введите {str}: "))
    while n <= 0:
        print(f"В наборе минимум 1 элемент! , повторите ввод {str}: ")
        n = int(input())
    return n 
def GetIntList(str,n):
    print(f"Введите {str}: ")
    numbers = []
    row = input()
    numbers = list(map(int, row.split()))
    while n != len(numbers):
        print(f"Введено неверное количество чисел, должно быть {n} , повторите попытку ввода")
        numbers = []
        row = input()
        numbers = list(map(int, row.split()))
    return numbers
def Process(str1 , str2):
    flag = 1
    str3 = [] 
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                for k in range(len(str3)):
                    if str1[i] == str3[k]:
                        flag = 0
                if flag == 1 :
                    str3.append(str1[i])
                else :
                    flag = 1
    return print(f"Встречаются в обоих наборах: {sorted(str3)}") 
Process(GetIntList("первое множество",GetInt("n")) ,(GetIntList("второе множество",GetInt("m"))))