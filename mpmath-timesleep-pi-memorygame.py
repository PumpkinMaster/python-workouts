"""

This game of pi tests how far the player can remember the numbers of Pi.
But I'm gonna do it in an app.
This is just the Python test test. Cheers.

"""
# import math
# pi = math.pi
# Not precise enough :(

import mpmath as mp
import time
import sys


def readyStart():
    print("\n-> Okay! Ready?")
    time.sleep(0.8)
    print("-> 1...")
    time.sleep(0.8)
    print("-> ...2...")
    time.sleep(0.8)
    print("-> ......3...")
    time.sleep(0.8)
    print("-> .........START!")
    time.sleep(1.2)


def consolation():
    print("\n-> So, how did you do? Did you get every one? ;)")
    try:
        play_again = input("-> Would you like to play again? (y/n) ")
        if not play_again.isalpha():
            raise Exception("\n-> Please enter letters only."
                            "\n-> Specifically 'y' or 'n' please.")
        else:
            if play_again != 'y' and play_again != 'n':
                raise Exception("\n-> Enter 'y' or 'n' only.")
    except Exception as error:
        print(error)
        return consolation()

    else:
        if play_again == 'y':
            main()
        else:
            print("\n-> Aww, sad to see you go. Come play again soon!")
            sys.exit()


def main():
    print("-> Let's play Pi Panic!")

    try:
        dp = int(input("-> Up to how many decimal places would you like to play? "))
        if dp <= 0:
            raise Exception("Hey, no integers less than 0.")
    except ValueError as e:
        print("ERROR: ", e)
        return main()
    except Exception as e:
        print(e)
        return main()

    else:
        readyStart()
        with mp.workdps(dp+1):
            print("\n-> ", end='')
            for x in str(mp.pi):
                print(x, end='')
                time.sleep(2)

        print("")
        consolation()


main()


# dir(math)
# to see what the module has.
