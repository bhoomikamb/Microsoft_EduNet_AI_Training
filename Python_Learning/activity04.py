#Activity-01
with open("grades.txt","w") as file:
    contents=file.write("""[("Akshata",80),("Bhoomika",75),("Cherry":65),("David":55),("Eve":35)]""")
    print(contents)
#Activity-02
import csv
total=0
with open("Python_Learning/products.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        total+=float[row("Price")]
print("Total cost of all products:",total)