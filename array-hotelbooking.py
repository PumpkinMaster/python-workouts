'''
Hotel Booking System: Array + Pre/Post Conditions
'''

# Part (a): double array to store booking status for one day.
booking_stat = [['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
                ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
                ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
                ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
                ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
                ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
                ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],     # 10 floors; 10x10 rooms
                ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],     # 'A' - vacant
                ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],     # 'B' - booked
                ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']]     # 'C' - checked in

floor_list = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10']
room_list = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10']


# Part (b): functions for receptionist/manager to update booking_stat.
def display_booking_stat():
    print("\n||==========================================================================||")
    print("||                               Booking Status                             ||")
    print("||==========================================================================||")
    print("||                                                                          ||")
    count = 0
    for floor in booking_stat:      # for each row
        print("||   ", end= "")        # start each row with '||'
        for room in floor[:-1]:      # for the 1st till the 9th element in current row/floor
            print("| %s |  " % (room), end="")
        print("| %s |   ||" % (floor[-1]), end="")      # prints last or 10th element of current row/floor
        print(" - %s" % (floor_list[count]))
        count += 1
    print("||                                                                          ||")
    print("||==========================================================================||")
    print("      ", end="")
    for elem in range(len(room_list)):
        print(room_list[elem], end= "     ")
    print("\n\t", end="")
    for tab in range(10):
        print("  --   ", end="")


def perform_booking():
    print("\n\n\n||=============================================||")
    print("||              Perform booking...             ||")
    print("||=============================================||")

    while True:
        try:
            num_of_rooms = int(input("\n>> Number of rooms: "))

            if num_of_rooms > 100 or num_of_rooms < 0:
                raise Exception("Invalid number of rooms.")

        except ValueError:
            print("\n>>> ERROR: Integers only.\n")
            continue
        except Exception as error:
            print("\n>>> ERROR:", error)
            continue

        count = 1
        for i in range(num_of_rooms):
            print("\n\n|| ROOM %d ||" % (count))
            try:
                book_floor = int(input("\n>>> Enter floor (Integers 1 to 10 only): "))

                if book_floor < 1 or book_floor > 10:
                    raise Exception("Invalid floor entered.")

            except ValueError:
                print("\n>>> ERROR: Integers only.")
                continue
            except Exception as error:
                print("\n>>> ERROR:", error)
                continue

            while True:
                try:
                    book_room = int(input("\n>> Which room? (Enter integers 1 to 10 only.\n>> "))
                except ValueError:
                    print("\n<< ERROR: Integers only >>\n")
                    continue
                break


            if booking_stat[book_floor - 1][book_room - 1] == 'B':
                print("<< Room is already booked. >>")
            else:
                booking_stat[book_floor - 1][book_room - 1] = 'B'
                print("\n>> ROOM %d booked successfully! " % (count))
            count += 1

        break
    # should the system display the booking stat immediately after?


def perform_check_in():
    print("\n\n\n||=============================================||")
    print("||              Perform Check-In...            ||")
    print("||=============================================||")

    while True:
        try:
            num_of_rooms = int(input("\n>> Number of rooms: "))
        except ValueError:
            print("\n>>> ERROR: Integers only.\n")
            continue
        except Exception as error:
            print("\n>>> ERROR:", error)
            continue

        count = 1
        for i in range(num_of_rooms):
            print("\n\n|| ROOM %d ||" % (count))
            try:
                check_in_floor = int(input("\n>> Which floor? (Enter integers 1 to 10 only.\n>> "))

                if check_in_floor < 1 or check_in_floor > 10:
                    raise Exception("1 to 10 only.")

            except ValueError:
                print("\n>>> ERROR: Integers only.\n")
                continue
            except Exception as error:
                print("\n>>> ERROR:", error)
                continue

            while True:
                try:
                    check_in_room = int(input("\n>> Which room? (Enter integers 1 to 10 only.\n>> "))

                    if check_in_room < 1 or check_in_room > 10:
                        raise Exception("1 to 10 only.")

                except ValueError:
                    print("\n<< ERROR: Integers only >>\n")
                    continue
                except Exception as error:
                    print("\n>>> ERROR:", error)
                    continue

                else:
                    break

            temp = booking_stat[check_in_floor - 1][check_in_room - 1]
            if temp == 'B':
                booking_stat[check_in_floor - 1][check_in_room - 1] = 'C'
                print("\n>> ROOM %d  successfully! " % (count))
                count += 1
            else:
                print("\n>>> Selected room has not been booked! Unable to check-in.")
                print("\n>>> Returning to main menu...")
                break

        break


def summary():
    empty_rooms = 0
    booked_rooms = 0
    checkedin_rooms = 0

    for i in booking_stat:
        for j in i:
            if j == 'A':
                empty_rooms += 1
            elif j == 'B':
                booked_rooms += 1
            else:
                checkedin_rooms += 1
    print("")
    print("==============================")
    print(" Summary of Daily Operations")
    print("")
    print(" Total bookings: %d" % (booked_rooms))
    print(" Total checked-in: %d" % (checkedin_rooms))
    print(" Total empty rooms: %d" % (empty_rooms))
    print("==============================")


def main_menu():
    print("")
    print("=======================================")
    print("|        Hotel Booking System         |")
    print("|                                     |")
    print("|   1. Display hotel booking status.  |")
    print("|   2. Perform booking.               |")
    print("|   3. Perform check-in.              |")
    print("|   4. Summary of daily operation.    |")
    print("|   5. Exit system.                   |")
    print("=======================================")

    try:
        option = int(input(">>> Enter option: "))

        if option < 1 or option > 5:
            raise Exception(" Invalid option entered.")

    except ValueError as error:
        print("\n>>> ERROR:", error)
        print(">>> Integers only.")
        return main_menu()
    except Exception as error:
        print("\n>>> ERROR:", error)
        return main_menu()

    else:
        if option == 1:
            display_booking_stat()
            print("")
            return main_menu()
        elif option == 2:
            perform_booking()
            print("")
            return main_menu()
        elif option == 3:
            perform_check_in()
            print("")
            return main_menu()
        elif option == 4:
            summary()
            return main_menu()
        else:
            print("\n>>> Exiting system.")
            return


main_menu()


