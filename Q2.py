"""
Student Database System
"""


class Student:

    def __init__(self, name=None, studentID=None, year_ob=None, intake=None, CGPA=None):
        self.__name = name
        self.__studentID = studentID
        self.__yob = year_ob
        self.__intake = intake
        self.__cgpa = CGPA
        self.studentsList = []
        self.quick_sort(self.studentsList, start=0, end=9)


    # Name : getter and setter
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    # Student ID : getter and setter
    def set_std_id(self, studentID):
        self.__studentID = studentID

    def get_std_id(self):
        return self.__studentID

    # Year of birth : getter and setter
    def set_yob(self, year_ob):
        self.__yob = year_ob

    def get_yob(self):
        return self.__yob

    # Intake : getter and setter
    def set_intake(self, intake):
        self.__intake = intake

    def get_intake(self):
        return self.__intake

    # CGPA : getter and setter
    def set_cgpa(self, CGPA):
        self.__cgpa = CGPA

    def get_cgpa(self):
        return self.__cgpa

    # Method to add new students.
    def add_student(self):
        students = self.studentsList
        student.set_name(input(">>> Enter name: "))
        student.set_std_id(input(">>> Enter student ID: "))
        student.set_yob(input(">>> Enter year of birth: "))
        student.set_intake(input(">>> Enter intake session: "))
        student.set_cgpa(input(">>> Enter current CGPA: "))
        students.append(student)
        print("\n>>> New student record has been added.")

    # Method to add the given 10 students.
    def preset_student(self):
        students = self.studentsList
        students.append(Student("Jesmine", 7304410, 1997, 'August 2017', 3.40))
        students.append(Student("Hashim", 7502291, 1998, 'January 2018', 2.60))
        students.append(Student("Clarin", 7402914, 1997, 'January 2018', 3.99))
        students.append(Student("Muhamad", 7432111, 1998, 'April 2018', 3.00))
        students.append(Student("Peter", 7380201, 1996, 'August 2017', 2.91))
        students.append(Student("Ashwin", 7402916, 1997, 'January 2018', 1.90))
        students.append(Student("Mashar", 7334902, 1996, 'August 2017', 3.20))
        students.append(Student("Albert", 7500899, 1998, 'April 2018', 4.00))
        students.append(Student("Yiling", 7456201, 1997, 'January 2018', 3.00))
        students.append(Student("Aishah", 7500984, 1998, 'April 2018', 4.00))

    # Linear Searching
    def search(self, criteria=None):
        std_list = self.studentsList
        for student_obj in std_list:
            # Criteria: Year of birth
            if type(criteria) == int:
                if student_obj.get_yob() == criteria:
                    print(student_obj.get_name(), student_obj.get_std_id())
            # Criteria: CGPA > 2.50
            elif type(criteria) == float:
                if student_obj.get_cgpa() > criteria:
                    print(student_obj.get_name(), student_obj.get_std_id(), student_obj.get_cgpa())
            # Criteria: Intake session
            elif type(criteria) == str:
                if student_obj.get_intake() == criteria:
                    print(student_obj.get_name(), student_obj.get_std_id(), student_obj.get_yob())

    def quick_sort(self, arr, start=0, end=9):
        std_list = self.studentsList
        if start < end:
            pivot = self.partition(std_list, start, end)

            self.quick_sort(std_list, start, pivot - 1)
            self.quick_sort(std_list, pivot + 1, end)

    def partition(self, std_list, start, end):
        box = std_list[end].get_cgpa()
        elem = start - 1
        for m in range(start, end+1):
            if std_list[m].get_cgpa() <= box:
                elem = elem + 1
                if elem < m:
                    temp = std_list[elem]
                    std_list[elem] = std_list[m]
                    std_list[m] = temp
        return elem

    """
    def display(self):
        std_list = self.studentsList

        for i in range(9):
            name = std_list[i].get_name()
            studentID = std_list[i].get_std_id()
            cgpa = std_list[i].get_cgpa()

            print("%s, %d, %.2f" % (name, studentID, cgpa))
    """

# Search OPTION
def search_option():
    print("")
    print("==========================")
    print("|    1. Year of birth    |")
    print("|    2. CGPA             |")
    print("|    3. Intake session   |")
    print("==========================")
    try:
        searchOption = int(input(">>> Search by criteria: "))

        if searchOption <= 0 or searchOption > 3:
            raise Exception("Select criteria 1, 2 or 3 only.")

    except ValueError as error:
        print("\n>>> ERROR: ", error)
        print(">>> Positive integers only.")
        return search_option()

    except Exception as error:
        print("\n>>> ERROR: ", error)
        return search_option()

    else:
        return searchOption


# Function for getting year of birth as search criteria.
# Returns to main_menu().
def yob_criteria():
    try:
        year_ob = int(input("\n>>> Enter year of birth: "))

        if len(str(year_ob)) != 4:
            raise Exception("Invalid year of birth.")

    except ValueError as error:
        print("\n>>> ERROR: ", error)
        print(">>> Year of birth must be 4 digits.")
        return yob_criteria()

    except Exception as error:
        print("\n>>> ERROR: ", error)
        return yob_criteria()

    else:
        return year_ob


# Function for getting validated CGPA.
# Returns to main_menu().
def cgpa_criteria():
    try:
        cgpa = float(input("\n>>> Enter CGPA: "))

    except ValueError as error:
        print("\n>>> ERROR: Enter numbers only.")
        return cgpa_criteria()
    except Exception as error:
        print("\n>>> ERROR:", error)
        return cgpa_criteria()

    else:
        return cgpa


# Function for getting validated intake session.
# Returns to main_menu().
def intake_criteria():
    intake_months = ['January', 'April', 'August']
    try:
        month = input("\n>>> Enter month: ")
        month = month.capitalize()

        if not month.isalpha():
            raise Exception(" Letters only.")
        elif month not in intake_months:
            raise Exception("Month entered is not valid."
                            " Enter months 'January', 'April' and 'August' only.")
    except Exception as error:
        print("\n>>> ERROR:", error)
        return intake_criteria()

    else:

        while True:
            try:
                year = int(input("\n>>> Enter year: "))
                if len(str(year)) != 4:
                    raise Exception(" The year you entered makes no sense.")

            except ValueError as error:
                print("\n>>> ERROR:", error)
                print(">>> Enter integers only.")
                continue
            except Exception as error:
                print("\n>>> ERROR:", error)
                continue

            else:
                break

        intake_session = month + " " + str(year)
        return intake_session

    # MAIN


def main_menu():
    print("==============================================")
    print("|          Student Database System           |")
    print("|                                            |")
    print("|        1. Enter new student record.        |")
    print("|        2. Search record.                   |")
    print("|        3. Sort and display.                |")
    print("|        4. Exit system.                     |")
    print("==============================================")
    try:
        option = int(input(">>> Enter option: "))

        if option <= 0 or option > 4:
            raise Exception("Invalid option entered.")

    except ValueError as error:
        print("\n>>> ERROR: ", error)
        print(">>> Correction: Positive integers only.")
        return main_menu()

    except Exception as error:
        print("\n>>> ERROR: ", error)
        print(">>> Correction: Enter option 1, 2, 3 or 4 only.")
        return main_menu()

    else:
        # User wants to add new student record.
        if option == 1:
            print("")
            Student.add_student(student)
            print("\n>>> Student successfully added.")
            return main_menu()

        # User wants to search for student by criteria.
        elif option == 2:
            search_criteria = search_option()
            print("")
            # Search by year of birth
            if search_criteria == 1:
                year_ob = yob_criteria()
                Student.search(student, year_ob)
                print("")
                return main_menu()
            # Search by CGPA
            elif search_criteria == 2:
                cgpa = cgpa_criteria()
                Student.search(student, cgpa)
                print("")
                return main_menu()
            # Search by intake session
            else:
                intake = intake_criteria()
                Student.search(student, intake)
                print("")
                return main_menu()

        # User wants to sort and display student records.
        elif option == 3:
            Student.quick_sort(student)
            # Student.display(student)
            return main_menu()

        # User wants to exit system.
        else:
            print("\n>>> Exiting system.")
            return


# For predetermined 10 students.
student = Student()
Student.preset_student(student)

# Print out a particular detail.
wow = student.studentsList[2]
print(wow.get_name())

# For making new students.
new_student = Student()
# Student.add_student(new_student)


main_menu()





