import csv
import sys
import copy
# filename ="/home/caratred/Learning/python/Student_marks_list.csv"

# opening the file using "with"
# statement
class_highest = []
sub_highest = {}
with open(sys.argv[1],'r') as f:
    
    for line in csv.DictReader(f):
        a = dict(line)
        stu_name = a['Name']
        del a['Name']
        if len(sub_highest)<1:
            sub_highest = copy.deepcopy(a)
            # name  = sub_highest['Name']
            # del sub_highest['Name']
            sub_highest = {key:[int(value),stu_name] for (key,value) in sub_highest.items()}
        else:
            # del a['Name']
            for k,v in a.items():
                if k!="Name":
                    if int(a[k])>sub_highest[k][0]:
                        sub_highest[k] = [int(v),stu_name]                
        total = sum(int(a[item]) for item in a)
        if len(class_highest)<3:
            class_highest.append([stu_name,total])
        else:
            class_highest.sort(key = lambda x: x[1],reverse=True) 
            if total>class_highest[0][1]:
                class_highest[0] = [stu_name,total]
            elif total>class_highest[1][1]:
                class_highest[1] = [stu_name,total]
            elif total>class_highest[2][1]:
                class_highest[2] = [stu_name,total]
            else:
                pass            




for each in sub_highest:
    print("Topper in "+each+" is  "+sub_highest[each][1])

print(" ")
print("Best Students in class are "+class_highest[0][0]+" with "+str(class_highest[0][1])+", "+class_highest[1][0]+" with "+str(class_highest[1][1])+", "+class_highest[2][0]+" with "+str(class_highest[2][1]))
