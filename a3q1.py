import psycopg2

def getAllStudents():
    cursor.execute("SELECT * FROM students;")
    print("PRINTING ALL STUDENTS:")
    for student in cursor:
        for attribute in student:
            print(attribute,end=" ")
        print("")
    print("")

def addStudent(first_name, last_name, email, enrollment_date): 
    print("")
    cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES(%s,%s,%s,%s);", (first_name,last_name,email,enrollment_date))
    connection.commit()

def updateStudentEmail(student_id, new_email):
    print("")
    cursor.execute("UPDATE students SET email=%s WHERE student_id=%s;",(new_email,student_id))
    connection.commit()

def deleteStudent(student_id):
    print("")
    cursor.execute("DELETE FROM students WHERE student_id=%s;",(student_id))
    connection.commit()

connection = psycopg2.connect(host='localhost', dbname="postgres", user="postgres",password="admin",port=5432)
cursor = connection.cursor()

# create table and add data
cursor.execute(open("intializer.sql","r").read())
connection.commit()

# prompt loop for users
while True:
    print("1: Get All Students")
    print("2: Add Student")
    print("3: Update a Students Email")
    print("4: Delete Student")
    print("5: Press Anything Else To Exit")

    selection = input("Select an operation:")

    if selection == '1':
        getAllStudents()
    elif selection == '2':
        fName = input("Enter Students First Name: ")
        lName = input("Enter Students Last Name: ")
        email = input("Enter Students Email: ")
        date = input("Enter Students Enrollment Date (ex: 2023-09-01):")
        addStudent(fName,lName,email,date)
    elif selection == '3':
        email = input("Enter Their New Email: ")
        id = input("Enter Their ID: ")
        updateStudentEmail(id,email)
    elif selection == '4':
        id = input("Enter Their ID:")
        deleteStudent(id)
    else:
        break
    print("")


cursor.execute("DROP TABLE students;")
connection.commit()

cursor.close()
connection.close()