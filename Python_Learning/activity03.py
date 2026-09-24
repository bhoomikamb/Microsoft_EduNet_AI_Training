#activity-01
student={"name":"akshata",
          "age":19,
          "grades":[80,90,60,70,98]}
print(student)
#activity-02
student["major"]="Electronics"
print("updated dictionary",student)
#activity-03
average=sum(student["grades"])/len(student["grades"])
print("Average grade:",average)