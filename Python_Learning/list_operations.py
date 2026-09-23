fruits=["mango","apple","banana","kivi"]   #Creating LIst
students=("Akshata","Bhoomika","Priya","Lanchana")  #Creating Tuple
print(fruits)
print(students)
fruits.append("Strawberry") #Adding item to List
print("updated list:",fruits)
fruits.remove("mango")  #Removing item from list
print(fruits)
print(fruits[0]) #access item by index
fruits[3]="guava"  #changing elements in list
print(fruits)
fruits.insert(2,"Custard") #Adding item to list by value
print(fruits)
print(len(fruits)) #length of list
print(fruits[2].upper()) #Upper
fruits.pop() #deleting element at last
print(fruits)