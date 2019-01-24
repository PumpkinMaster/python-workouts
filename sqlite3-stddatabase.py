# Creating Student database and record table.
import sqlite3
conn = sqlite3.connect('Student.db')
c = conn.cursor()
print ("<<Student database created successfully>>")

conn.execute('''CREATE TABLE RECORD
(STUDENT_ID  INT  PRIMARY KEY   NOT NULL,
STUDENT_NAME  TEXT   NOT NULL,
SCHOOL  CHAR(50)   NOT NULL,
STUDY_YEAR  INT  NOT NULL);''')

print ("<<Table record created successfully>>")
print ("  .  \n  .  \n  .  ")

# Entering records using multiple inserts.
insert_into = "INSERT INTO RECORD VALUES (?,?,?,?)"
students1 = [(1001, 'Stella', 'St George', 1), (1002, 'Evon', 'St Paul', 2),
             (1003, 'Steven', 'Prince Wales', 1), (1004, 'Chin Fong', 'St Paul', 2),
             (1005, 'Joshua', ' St Paul', 3), (1006, 'Albert', 'Prince Wales', 3),
             (1007, 'Ming Zhen', 'St George', 2), (1008, 'Sherlyn', 'St Paul', 2),
             (1009, 'Johnny', 'St Paul', 3)]
conn.executemany(insert_into, (students1))  # Way to prevent SQL Injection.

print ("<<9 records has been entered into table>>")
print ("\n\n\n<<Entering DATABASE MENU>>\n\n\n")


# Menu for database.
def mainMENU():
    print ("            [Excel Tuition Center's DATABASE]              ")
    print ("***********************************************************")
    print ("*                                                         *")
    print ("*   SEARCH record                   -  Press '1'          *")
    print ("*   CREATE new record               -  Press '2'          *")
    print ("*   DISPLAY all existing records    -  Press '3'          *")
    print ("*                                                         *")
    print ("*   EXIT database                   -  Press '0'          *")
    print ("*                                                         *")
    print ("***********************************************************")
    print ("\n")
    print ("Hello, I'm Serena! This database's interface~\n")
    option = input("Is there anything that I can help you with? Please enter your option:  ")
    print ("\n")
    if option == '1':
        search()
    elif option == '2':
        create()
    elif option == '3':
        display()
    elif option == '0':
        print ("<<EXITING database...>><<Please come again~>>")
    else:
        print ("Invalid option entered. Please try again~")
        mainMENU()



# SEARCH record.
def search():
    print ("")
    print ("*******************************************")
    print ("* How would you like to search? By:       *")
    print ("*                                         *")
    print ("* Student ID           -  Press '1'       *")
    print ("* Student Name         -  Press '2'       *")
    print ("* School               -  Press '3'       *")
    print ("* Study Year           -  Press '4'       *")
    print ("*                                         *")
    print ("* Return to main menu  -  Press '0'       *")
    print ("*******************************************")
    print ("")
    searchBy = input("Enter option:  ")
    if searchBy.isdigit():
        searchBy = int(searchBy)
        if searchBy == 1:
            print (" ")
            student_ID()
        elif searchBy == 2:
            print (" ")
            
            student_name()
        elif searchBy == 3:
            print (" ")
            school()
        elif searchBy == 4:
            print (" ")
            study_year()
        elif searchBy == 0:
            print ("  .\n  .\n  .\n<<Returning to MAIN MENU>>\n  .\n  .\n  .\n")
            mainMENU()
        else:
            print ("\n<<ERROR>><<Invalid option>><<ERROR>>\n")
            search()
    else:
            print ("\n<<Invalid option entered>><<Please try again~>>\n")
            search()

# Search by study year
def study_year():
    study_year = input("Students who are at study year:  ")
    print ("\n")
    if study_year.isdigit():
        study_year = int(study_year)
        if study_year>0 and study_year<4:
            print ("Here are the students who are at study year %s~" % (study_year,))
            matched = c.execute('''SELECT STUDENT_NAME,SCHOOL FROM RECORD WHERE STUDY_YEAR=?''' ,(study_year))
            for row in matched:
                print (row)
            print (" ")
            whatnow = input("Would you like to search again? Enter 'yes' or 'no':  ")
            if whatnow == 'yes':
                print (" ")
                search()
            else:
                print ("  .\n  .\n  .\n<<Returning to MAIN MENU>>\n  .\n  .\n  .\n")
                mainMENU()
        else:
            print ("\n<<ERROR>><<Study Year does not exist>><<Please try again>>\n")
            search()
    else:
        print ("\n<<ERROR>><<Study Year must be an integer>><<ERROR>>")
        print ("\n<<Failure to search>><<Please try again>>\n")
        search()
        
# Search by student name        
def student_name():
    student_name = input("Name of student:  ")
    student_name = student_name.title()
    print (" ")
    matched = c.execute('''SELECT * FROM RECORD WHERE STUDENT_NAME=?''' ,(student_name,))
    for row in matched:
        print (row)
    print (" ")
    whatnow = input("Would you like to search again? Enter 'yes' or 'no':  ")
    if whatnow == 'yes':
        print (" ")
        search()
    else:
        print ("  .\n  .\n  .\n<<Returning to MAIN MENU>>\n  .\n  .\n  .\n")
        mainMENU()

# Search by student ID
def student_ID():
    studentID = input("Student ID:  ")
    print (" ")
    matched = c.execute('''SELECT * FROM RECORD WHERE STUDENT_ID=?''' ,(studentID,))
    for row in matched:
        print (row)
    print (" ")
    whatnow = input("Would you like to search again? Enter 'yes' or 'no':  ")
    if whatnow == 'yes':
        print (" ")
        search()
    else:
        print ("  .\n  .\n  .\n<<Returning to MAIN MENU>>\n  .\n  .\n  .\n")
        mainMENU()

# Search by school
def school():
    school = input("School:  ")
    school = school.title()
    print (" ")
    matched = c.execute('''SELECT * FROM RECORD WHERE SCHOOL=?''', (school,))
    for row in matched:
        print (row)
    print (" ")
    whatnow = input("Would you like to search again? Enter 'yes' or 'no':  ")
    if whatnow == 'yes':
        print (" ")
        search()
    else:
        print ("  .\n  .\n  .\n<<Returning to MAIN MENU>>\n  .\n  .\n  .\n")
        mainMENU()


# CREATE record.
def create():
    std_name = input("Name of student: ")
    std_name = std_name.title()
    std_school = input("School of student: ")
    std_school = std_school.title()
    study_year = input("Student's study year: ")
    if study_year.isdigit():
        study_year = int(study_year)
        if study_year>0 and study_year<4:
            std_ID = c.execute('''SELECT COUNT(STUDENT_ID) FROM RECORD''')
            for i in std_ID:
                std_ID = int (i[0]) + 1001
            insert_into = "INSERT INTO RECORD VALUES (?,?,?,?)"
            conn.execute(insert_into, (std_ID,std_name,std_school,study_year))
            print ("  .  \n  .  \n  .  ")
            print ("<<Student %s's records inserted into table successfully>>" % (std_name))
            print ("\n\n")
            whatnow = input("Would you like to enter another record? Enter 'yes' or 'no':  ")
            if whatnow == 'yes':
                print (" ")
                create()
            elif whatnow == 'no':
                print ("  .\n  .\n  .\n<<Returning to MAIN MENU>>\n  .\n  .\n  .\n")
                mainMENU()
            else:
                print ("\n<<ERROR>><<Invalid entry:'yes' or 'no' only>><<ERROR>>\n")
                print ("<<Auto-returning to MAIN MENU>>")
        else:
            print ("\n<<ERROR>><<Study Year '1', '2' and '3' only>><<Please try again>>\n")
            create()
    else:
        print ("\n<<ERROR>><<Study Year must be an integer>><<ERROR>>")
        print ("\n<<Failure to create new student record>><<Please try again>>\n")
        print ("  .\n  .\n  .\n<<Returning to MAIN MENU>>\n  .\n  .\n  .\n")
        mainMENU()
    


# DISPLAY record.
def display():
    print ("<<Displaying>>\n  . \n  . \n  . \n")
    print ("Here are all existing records~")
    print (" ")
    all_records = c.execute('''SELECT * FROM RECORD''')
    for row in all_records:
        print (row)
    print ("  .\n  .\n  .\n<<Returning to MAIN MENU>>\n  .\n  .\n  .\n")
    mainMENU()


# Call Main Menu.
mainMENU()
    
conn.commit()
conn.close()
    
