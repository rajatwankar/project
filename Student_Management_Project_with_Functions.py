
class Student:
    def __init__(self, r, n, m): #self = s, rollno = r, name = n, marks = m
        self.rollno = r 
        self.name = n
        self.marks = m

    def __str__(self):
        return f"ROLL NO.: {self.rollno}, "\
               f"NAME : {self.name}, "\
               f"MARKS : {self.marks}"

student_list = []

def add_student():
    rollno = int(input("Enter Roll No. :"))
    name = input("Enter Name:")
    marks = float(input("Enter Marks"))

    s = Student(rollno, name, marks) # as soon as the object is created init method
                                     #is called i.e rollno = r, name = n, marks = m
    student_list.append(s)
    print("STUDENT ADDED")

def show_student():
    print("ALL STUDENTS")
    for student in student_list:
        print(student)# as we are printing the objects __str__ is called

def check_student():
    rn = int(input("Enter Roll no to be checked: "))

    for student in student_list:
        if student.rollno == rn: # we check if student with entered rollno is present in
                                 # list or not
            return student    #we return Student objects like s1,s2,s3 etc

def delete_student():
    result = check_student()  #here result = student objects(s1,s2,s3 etc)

    if result:
        student_list.remove(result)
    else:
        print("NO SUCH STUDENT FOUND")
    print("STUDENT DELETED")

def update_student():
    result = check_student()
    if result:
        choice = int(input("Enter the basis on which you want to "\
                            "update :\n1.NAME\t\t2.MARKS"))
        match choice:
                    case 1:
                        newname = input("Enter Name to be"\
                                             "Updated:")

                        result.name = newname  #internally, object.name = newname i.e
                                            #we initialize variable name hence it changes name

                        print("STUDENT NAME UPDATED")
                                    
                    case 2:
                        newmarks = float(input("Enter Marks to "\
                                          "be updated"))

                        result.marks = newmarks  #internally, object.marks = newmarks
                                    #we initialize variable marks hence it changes marks

                        print("STUDENT NAME UPDATED")
                                    
    else:
        print("NO SUCH STUDENT FOUND")


while True:
    choice = int(input("\nEnter Choice : \n1. ADD STUDENT\
                       \t2. SHOW ALL STUDENT\
                   \n3. DELETE STUDENT\t\t\t4. UPDATE STUDENT \
                   \n5. EXIT"))
    match choice:
                 case 1:
                     add_student()
                     

                 case 2:
                     show_student()

                 case 3:
                     delete_student()

                 case 4:
                     update_student()

                 case 5:
                     print("EXIT")
                     break

                 case _:
                     print("INVALID CHOICE")


