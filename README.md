DESCRIPTION:
This is a simple Python application that connects to a PostgreSQL database and allows you to perform basic CRUD operations.

SOFTWARE REQUIRED:
	1. Python 3 installed  (https://www.python.org/downloads/)

	2. PostgreSQL installed and running  
		For Mac (https://www.postgresql.org/download/macosx/)
		For Windows (https://www.postgresql.org/download/windows/)

	3. psycopg2-binary Python package installed using the command 'python3 -m pip install psycopg2-binary'

FILES INCLUDED:
	a3_app.py
	students.sql

HOW TO COMPILE & RUN:
	1. Create a database with the name you like that will be referenced as DB_name in Postgre.SQL
	
	2. Use the students.sql file to create and populate a students table within your database

	3. Update the a3_app.py connectDB() function by changing the 'database="INSERT_DB_NAME"' to  'database="DB_name"' by using the database name you created.

	4. Update the a3_app.py connectDB() function by changing the 'password="INSERT_POSTGRE_PASSWORD"' by inserting your password.

	5. Finally, in the terminal/command prompt direct yourself to where you have the updated a3_app.py saved and use the command "python3 a3_app.py" to run the application

	6. Once you run the program you should be treated and prompted to enter 'c' to continue. Once done you should see a menu that looks like this to be able to edit your DB.

==== DATABASE OPTIONS MENU ====
1. View all students
2. Add a new student
3. Update a student's email
4. Delete a student
5. Exit application
Enter your choice (1-5):

NOTES & TIPS:

- student_id is automatically generated and unique (primary key)
- email must also be unique
- first_name and last_name are text and cannot be empty
- enrollment_date must be a valid date in YYYY-MM-DD format.
- each function opens and closes its own connection to prevent connections from staying open
 
TROUBLESHOOTING:

- if you encounter "connection to server at "localhost" (::1), port 5432 failed: FATAL:  database "DB_name" does not exist" error, ensure PostgreSQL is running and that the host, database, user, password and port in connectDB() are correct and match your system.
- if you encounter a "ModuleNotFoundError" error, ensure step 3 under SOFTWARE REQUIRED is done correctly, a uninstall and reinstall may be required
