# ==========================================
# Student Record System 
# ==========================================


# Global list to store all student records
students=[]

# ==========================================
# Function: Add Student
# Purpose: Add a new student into the system
# ==========================================
def add_student():
    print("\n --- Add Student ---")
    # Taking Roll Number input form the user 
    roll_num=int(input("Enter your Roll Number:"))
    # Checking Duplicate to avoid Duplication conflict
    for student in students:
        if student["Roll Number"]==roll_num:
            print("Studnet already exsists with this Roll Number:")
            return
    # Taking remaing details form the user
    name=input("Enter your Name:")
    Mis_id=int(input("Enter MIS ID:"))
    age=int(input("Enter you're Age:"))
    Department=input("Enter your Department:")
    Semester=input("Enter your Semester:")
    Section=input("Enter your Section:")
    # Adding the detials to the List
    students.append({
    "Roll Number": roll_num,
    "Name": name,
    "MIS ID": Mis_id,
    "Age": age,
    "Department": Department,
    "Semester": Semester,
    "Section": Section
    
})


        
# ==========================================
# Function: Display Students
# Purpose: Show all stored student records
# ==========================================

def display_students():
    print("\n --- Display Students --- ")
    
    # if no student found print the masg and exit
    if not students:
        print("No Records Found!")
    # Loop through all students and display their data
    for student in students:
        print("\n -------------------------------------")
        print(f"Roll Number:{student['Roll Number']}")
        print(f"Name:{student['Name']}")
        print(f"MIS ID:{student['MIS ID']}")
        print(f"Age:{student['Age']}")
        print(f"Department:{student['Department']}")
        print(f"Semester:{student['Semester']}")
        print(f"Section:{student['Section']}")
        print("\n -------------------------------------")
        
# ==========================================
# Function: Search Student
# Purpose: Find a student using roll number
# ==========================================
def search_student():
    # Taking Roll Number to search 
    print("\n --- Searching for Students --- ")
    roll_num=int(input("Enter Your Roll Number:"))
    # Searching in list 
    for student in students:
        if student['Roll Number']==roll_num:
               print("\n -------------------------------------")
               print(f"Roll Number:{student['Roll Number']}")
               print(f"Name:{student['Name']}")
               print(f"MIS ID:{student['MIS ID']}")
               print(f"Age:{student['Age']}")
               print(f"Department:{student['Department']}")
               print(f"Semester:{student['Semester']}")
               print(f"Section:{student['Section']}")
               print("\n -------------------------------------")
               return 
    print("Record not Found!")
    
            

# ==========================================
# Function: Update Student
# Purpose: Modify existing student data
# ==========================================
def update_student():
    print("\n --- Update Student --- ")
    # Input Roll Number of Student to Update
    roll_number=int(input("Enter your Roll Number:"))
    # Checking the roll number is exsist in the list 
    for student in students:
        if student['Roll Number']==roll_number:
            print("Enter new Details:")
            student['Name']=input("Enter New name:")
            student['MIS ID']=int(input("Enter New MIS ID:"))
            student['Age']=int(input("Enter new Age:"))
            student['Department']=input("Enter New Department:")
            student["Semester"]=input("Enter new Semester:")
            student['Section']=input("Enter new Section:")
            print("Record Updataed Successfully!")
            return
    # if not Found
    print("Record not Found!")
    
# ==========================================
# Function: Delete Student
# Purpose: Remove a student record
# ==========================================

def delete_student():
    print("\n --- Delete Student --- ")
    roll_number=int(input("Enter the Roll Number:"))
    for student in students:
        if student['Roll Number']==roll_number:
            students.remove(student)
            print("Student Record Deleted Successfullly!")
            return
    
    print("Record not Found!")
    
# ==========================================
# Main Menu Loop
# Purpose: Control center of the system
# ==========================================
while True:
     print("\n=================================")
     print("     Student Record System")
     print("=================================")

    # Menu options
     print("1. Add Student")
     print("2. Display Students")
     print("3. Search Student")
     print("4. Update Student")
     print("5. Delete Student")
     print("6. Exit")
     
     choice=input("Enter your choice form (1-6):")
     
     if choice=="1":
         add_student()
     elif choice=="2":
         display_students()
     elif choice=="3":
         search_student()
     elif choice=="4":
         update_student()
     elif choice=="5":
         delete_student()
     elif choice=="6":
         print("Program Ended!")
         print("Thanks for using the System")
     else:
         print("Invalid Choice, Try Again!")
    
        
    
        
        
         
        
            
    

    
