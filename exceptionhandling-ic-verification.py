from datetime import datetime

state_codes = ['01', '21', '22', '23', '24', '02', '25', '26', '27', '03', '28', '29',
               '04', '30', '05', '31', '59', '06', '32', '33', '07', '34', '35', '08',
               '36', '37', '38', '39', '09', '40', '10', '41', '42', '43', '44', '11',
               '45', '46', '12', '47', '48', '49', '13', '50', '51', '52', '53', '14',
               '54', '55', '56', '57', '15', '58', '16', '82']


def ic_handling():
    try:
        ic = input("\n>>> Enter your Identification Number (e.g. 123456121234): ")

        if not ic.isdigit():
            raise Exception(" Integers only.")
        elif len(ic) != 12:
            raise Exception(" IC number must be 12 digits long.")
        elif ic[6:8] not in state_codes:
            raise Exception(" Invalid STATE code.")

    except Exception as error:
        print("\n>>> ERROR:", error)
        return ic_handling()

    else:  # should I put the else statement inside?
        return ic



def age_handling():
    try:
        age = int(input(">>> Enter your age: "))

        if age <= 0 or age > 150:
            raise Exception(" The age you entered is unreasonable.\n"
                            ">>> Please enter your real age.")

    except ValueError as error:
        print("\n>>> ERROR: ", error)
        print(">>> Please enter integers only.")
        return age_handling()

    except Exception as error:
        print("\n>>> ERROR: ", error)
        return age_handling()

    else:
        return age


def gender_handling():
    try:
        gender = input(">>> Enter your gender ('male' or 'female'): ")

        # Exception Handling Event #1
        # the value entered contains non-alphabetic values.
        if not gender.isalpha():
            raise Exception("The gender you entered contains non-alphabetic values.\n"
                  ">>> Please enter 'male' or 'female' only.\n")
        else:
            gender.lower()

            # Program will accept 'm' as 'male' and 'f' as 'female'.
            if gender is 'm' or gender is 'f':
                if gender is 'm':
                     gender = "male"
                     return gender
                else:
                    gender = "female"
                    return gender

            # Exception Handling Event #2
            # In case user enters alphabetic values like 'mangoes' or 'fishcake'.
            elif gender != "male" and gender != "female":
                raise Exception("'%s' is not a valid input.\n"
                      ">>> Please enter 'male' or 'female' only.\n" % (gender))

    except Exception as error:
        print("\n>>> ERROR: ", error)
        return gender_handling()

    else:
        # All is well.
        return gender


# IN: Validated 'ic'
# OUT: 'yyyy-mm-dd'
def date_ob(ic):

    try:
        today_year = str(datetime.today())[2:4] # get last 2 digits of actual year.

        # first case -> 2000 and above
        if int(ic[:2]) <= int(today_year):

            if ic[:2] == "00":
                year_ob = "2000"
                date_ob = year_ob + "-" + ic[2:4] + "-" + ic[4:6]
                return date_ob  # e.g. '2000-mm-dd'

            else:
                year_ob = "20" + ic[:2]
                date_ob = year_ob + "-" + ic[2:4] + "-" + ic[4:6]
                return date_ob  # e.g. '2007-mm-dd' or '2012-mm-dd'

        # second -> 1900s
        else:
            year_ob = "19" + ic[:2]
            date_ob = year_ob + "-" + ic[2:4] + "-" + ic[4:6]
            return date_ob  # e.g. '1995-mm-dd'

    except TypeError as error:
        print("\n>>> ERROR:", error)
        return


# IN: date_ob
# OUT: age according to ic.
def age_from_ic(date_ofBirth):
    date_ofBirth = datetime.strptime(date_ofBirth, '%Y-%m-%d')
    age_fromIC = int((datetime.today() - date_ofBirth).days / 365)
    return age_fromIC


# IN: age and age_fromIC
# OUT: True or False
def age_consistency(age, age_from_ic):
    age_consistent = False
    try:
        if age != age_from_ic:
            raise Exception(" You said you're %d but your IC says you're %d." % (age, age_from_ic))

    except Exception as error:
        print("\n>>> ERROR:", error)

    else:
        age_consistent = True
        print("\n>>> Age is consistent with IC: %s" % (age_consistent))


def gender_consistency(ic, gender):
    gender_consistent = False
    try:
        # Males are ODD
        if int(ic[-1]) % 2 != 0:
            if gender != 'male':
                raise Exception(" You said you're MALE but your IC says you're FEMALE.")

        # Females are EVEN
        else:
            if gender != 'female':
                raise Exception(" You said you're FEMALE but your IC says you're MALE.")

    except Exception as error:
        print(">>> ERROR:", error)

    else:
        gender_consistent = True
        print(">>> Gender is consistent with IC: %s" % (gender_consistent))


def main_menu():
    ic = ic_handling()
    dob = date_ob(ic)
    ageFromIC = age_from_ic(dob)

    age = age_handling()

    gender = gender_handling()

    # Checking for age and gender consistency.
    age_consistency(age, ageFromIC) # prints True or ERROR
    gender_consistency(ic, gender)  # prints True or ERROR


main_menu()