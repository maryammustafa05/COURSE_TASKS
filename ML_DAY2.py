class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.grades={}
    def add_grade(self,subject,marks):
        self.grades[subject]=marks
    def calculate_avg(self):
        total=0
        count=0
        for mark in self.grades:
            total+=self.grades[mark]
            count+=1
        avg=total/count
        return avg
    def assign_grade(self,res):
        if(res>80):
           return "A"
        elif(res>79 and res<60):
           return "B"
        elif(res>59 and res<40):
            return "C"
        else:
            return "F"
    def apply_bonus(self):
        self.grades=dict(map(lambda item:(item[0],min(item[1]+5,100)),self.grades.items()))
    def generate_report(self):
        avg=self.calculate_avg()
        grade=self.assign_grade(avg)
        report=f"""
            "Name: " {self.name} 
            "Age: " {self.age}\n
"""
        for subject, marks in self.grades.items():
              report += f"\"{subject}: \" {marks}\n"
        report += f"\"Average: \" {avg:.2f}\n\"Grade: \" {grade}"
        return report
    def save_to_file(self,filename):
        f=open(filename,"w")
        f.write(self.generate_report())
    @staticmethod
    def load_from_file(filename):
        f=open(filename,"r")
        print(f.read())

name=input("enter student name: ")
age=(int(input("enter student age: ")))
st=Student(name,age)
subjects=["math","english","urdu"]
for s in subjects:
    marks=int(input(f"enter marks for {s}: "))
    st.add_grade(s,marks)
choice=input("Add bonus to your subjects?(yes/no)")
if(choice=="yes"):
    st.apply_bonus()
file=f"{name}_report.txt"
st.save_to_file(file)
print("REPORT CARD\n")
st.load_from_file(file)