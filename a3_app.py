import psycopg2 # used to access PostgreSQL
import sys  # used to exit for some errors

# connects to postgressDB
def connectDB():

    try:
        connection = psycopg2.connect(      # establishing conection with PostgreSQL
            host="localhost",
            database="INSERT_DB_NAME",      # insert your DB name
            user="postgres",
            password="INSERT_POSTGRE_PASSWORD", # insert your DB password
            port="5432"
        )
        return connection # successful connection established
    except Exception as e:
        print("Error connecting to database, application terminated", e)       # error flag to indicate no connection made
        sys.exit(1)


# will retrieve and prints all rows from the students table.
def getAllStudents():
    connection = None   # clear connection
    cursor = None       # clear cursor

    connection = connectDB()
    if connection is None:
        return  # exit if connection failed

    try:
        cursor = connection.cursor()  # open cursor connection

        # gets query to get all students
        cursor.execute("SELECT student_id, first_name, last_name, email, enrollment_date FROM students;")
        rows = cursor.fetchall()

        # print to screen results
        print("\n--- All Students ---")
        if rows:
            for row in rows: #row display formatting for app user
                print(f"ID: {row[0]}, Name: {row[1]} {row[2]}, Email: {row[3]}, Enrollment Date: {row[4]}")
        else:
            print("No students found.")     

        # close cursor and connection 
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    except Exception as e:
        print("Error retrieving students:", e) 
    
    finally:    # finally to ensure everything opened gets closed 
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# will collect student information and add a student in students
def addStudent(first_name, last_name, email, enrollment_date):
    connection = None   # clear connection
    cursor = None       # clear cursor

    try:
        connection = connectDB()        # open DB connection
        cursor = connection.cursor()    # open cursor connection

        insert_query = """      
            INSERT INTO students (first_name, last_name, email, enrollment_date)
            VALUES (%s, %s, %s, %s);
        """
        #sends off insert query to PostgreSQL
        cursor.execute(insert_query, (first_name, last_name, email, enrollment_date))
        connection.commit()

        print("Student added successfully.")    # confirmation flag for user

    except Exception as e:
        print("Error adding student:", e)       # error flag for user

    finally:    # finally to ensure everything opened gets closed 
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# will collect new email to update a student email in students (unique)
def updateStudentEmail(student_id, new_email):
    connection = None   # clear connection
    cursor = None       # clear cursor

    try:
        connection = connectDB()        # open DB connection
        cursor = connection.cursor()    # open cursor connection

        update_query = """
            UPDATE students
            SET email = %s
            WHERE student_id = %s;
        """
        #sends off update query to PostgreSQL
        cursor.execute(update_query, (new_email, student_id))
        connection.commit()

        print("Student email was updated successfully.")        # success flag for user

    except Exception as e:
        print("Error could not update student email:", e)       # error flag for user

    finally:    # finally to ensure everything opened gets closed 
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# will delete a student in students using their student ID
def deleteStudent(student_id):
    connection = None   # clear connection
    cursor = None       # clear cursor

    try:
        connection = connectDB()        # open DB connection
        cursor = connection.cursor()    # open cursor connection

        delete_query = """
            DELETE FROM students
            WHERE student_id = %s;
        """
        # sends off delete query to PostgreSQL
        cursor.execute(delete_query, (student_id,))
        connection.commit()

        print(f"Student with ID {student_id} deleted successfully.")    # confirmation flag for user

    except Exception as e:
        print("Error deleting student:", e)     # error flag for user

    finally:
        if cursor:    # finally to ensure everything opened gets closed 
            cursor.close()
        if connection:
            connection.close()


# main function including simple menu to help test CRUD functions
def main():
    print("Welcome to the Database Modification App")       # welcome statement
    choice = input("Enter c to continue: ").strip().lower()     # choice added to make entering app more oficcial

    if choice == 'c': # if c is inputted program will execute, if not it will terminate
        
        while True: # while loop that will show the menu options until program is quit
            print("\n==== DATABASE OPTIONS MENU ====")
            print("1. View all students")
            print("2. Add a new student")
            print("3. Update a student's email")
            print("4. Delete a student")
            print("5. Exit application")

            choice = input("Enter your choice (1-5): ").strip()

            if choice == '1':
                getAllStudents()  # calls get function

            elif choice == '2':
                print("\n--- Add New Student ---")      # prompts and starts to collect user input for new student
                first_name = input("Enter first name: ").strip()
                last_name = input("Enter last name: ").strip()
                email = input("Enter email: ").strip()
                enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ").strip()
                addStudent(first_name, last_name, email, enrollment_date) # sends the new student information to the addStudent function that will send it off to the DB

            elif choice == '3':
                print("\n--- Update Student Email ---")     # prompts and collects user for a student ID and new email
                student_id = input("Enter student ID to update: ").strip()
                new_email = input("Enter new email: ").strip()
                updateStudentEmail(student_id, new_email)   # sends the new email information to the updateStudentEmail function that will send it off to the DB

            elif choice == '4':
                print("\n--- Delete Student ---")    # prompts and collects student ID to delete 
                student_id = input("Enter student ID to delete: ").strip()
                deleteStudent(student_id)   # sends the student ID to the deleteStudent function that will send the deletion query to the DB

            elif choice == '5':
                print("\nApplication successfully closed.")     # exit application flag for user
                break  # exits the while loop

            else:
                print("\nInvalid choice. Please enter a number between 1 and 5.")   # instruction to prompt user in making a valid input
    else:
        print("Ok you did not want to continue...")     # funny easteregg for myself if a user doesnt input c to continue


main()