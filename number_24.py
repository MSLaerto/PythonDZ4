"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.
"""

import random as rnd

class Node:   
  def __init__(self,data):   
    self.data = data;   
    self.next = None;   
    
class CreateList:     
  def __init__(self):   
    self.head = Node(None);   
    self.tail = Node(None);   
    self.head.next = self.tail;   
    self.tail.next = self.head;   
         
  def add(self,data):   
    newNode = Node(data);     
    if self.head.data is None:     
      self.head = newNode;   
      self.tail = newNode;   
      newNode.next = self.head;   
    else:      
      self.tail.next = newNode;     
      self.tail = newNode;     
      self.tail.next = self.head;   
    
  def display(self):
    harvest_max = 0   
    current = self.head;   
    if self.head is None:   
      print("List is empty");   
      return;   
    else:   
        print("Урожай на каждом из кустов: ");      
        print(current.data , end = " "),   
        while(current.next != self.head):   
            current = current.next;   
            print(current.data , end = " "),
    #
    current = self.head
    second = current.next
    third = second.next
    harvest_current = current.data + second.data + third.data
    if harvest_max < harvest_current :
       harvest_max = harvest_current
    while(current.next != self.head):
        current = current.next
        second = current.next
        third = second.next
        harvest_current = current.data + second.data + third.data
        if harvest_max < harvest_current :
            harvest_max = harvest_current
            current_max = current.data
            second_max = second.data 
            third_max = third.data 
    print(f"\nМаксимальное число ягод на 3х сосдених кустах = {harvest_max} ({current_max}+{second_max}+{third_max})")
 
class CircularLinkedList:   
    cl = CreateList()
    data = []
    with open("blueberry_bush_harvest.txt") as f:
        for line in f:
            data.append([int(x) for x in line.split()])
    for i in range (len(data[0])):
       cl.add((data[0][i]))                 
    cl.display()

