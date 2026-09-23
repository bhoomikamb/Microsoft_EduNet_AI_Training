students=["Alice","Bob","Charlie","David","Eve"]#creating list
students.reverse()#revrse order of list
print("Reversed Order of list",students)
fruits=["Apple","Banana","Cherry","Date","fig","Grape"]
print(fruits[2:5])#list slicing
fruits.insert(3,"Strawberry")#adding item to the list by position
print(fruits)
ages=[23,45,18,34,60,50,27]
average=sum(ages)/len(ages)
print("Average:",average)
print(max(ages)) #highest number in list
print(min(ages))#lowest number in list
print(len(ages))#length of list
fruits.pop(5)#Deleting last element or by index
ages.remove(60) #Delete by index
print(ages)
fruits.remove("Cherry") #Delete by index 
print(fruits)