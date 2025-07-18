name=input("enter your name: ")
age=int(input("enter your age: "))

subjects={}
subjects["english"]=int(input("enter english marks: "))
subjects["maths"]=int(input("enter math marks: "))
subjects["urdu"]=int(input("enter urdu marks: "))

def calc_avg(x,y,z):
    avg=(x+y+z)/3
    return avg

res=calc_avg(subjects['english'],subjects['urdu'],subjects['maths'])

if(res>80):
    grade="A"
elif(res>79 and res<60):
   grade="B"
elif(res>59 and res<40):
   grade="C"
else:
    grade="F"

choice=input("Add bonus to your subjects?(yes/no)")
if(choice=="yes"):
    new_dict=dict(map(lambda item:(item[0],item[1]+5),subjects.items()))

report=f"""
"Name: " {name} 
"Age: " {age}
"Math: " {subjects['maths']}
"English: " {subjects['english']}
"Urdu: " {subjects['urdu']}
"Average: " {res}
"Grade: " {grade}
"""
f=open("report.txt","w")
f.write(report)
f=open("report.txt","r")
print("REPORT CARD")
print(f.read())