students={"name":"bhoomika",
          "course":"be",
          "age":19,
          "branch":"ece",
          "college":"mit",
          "cgpa":9}
print("\n")
print("Created dictionary",students)
print("Value of key:",students["name"])
print("Copying dictionary:",students.copy())
stud=students.fromkeys(students)
print("New dictionary with supplier keys:",stud)
print("New dictionary with default value:",students.fromkeys(students,4))
print("getting value by key:",students.get("branch"))
print("Objects of dictionary:",students.items())
print("Getting only keys:",students.keys())
print("getting only values of dictionary:",students.values())
print("deleting by key:",students.pop("college"))
print("updated dictionary:",students)
print("getting phela value:",students.pop("college",4))
print("removing random item:",students.popitem())
print("returning value of key:",students.setdefault("name"))
print("adding items:",students.setdefault("college","mit"))
#print("add new item:",students.update("sgpa":8.4))
print("Empty dictionary:",students.clear())