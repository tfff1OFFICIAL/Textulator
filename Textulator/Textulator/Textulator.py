import sys, math, os
from math import *
# Hopefully, this will work for both versions of python (2 and 3)
def uInput(text = ""):
    majorVersion = sys.version.split(".")[0]
    if majorVersion == '3':
        return input(text)
    else:
        return raw_input(text)

info = [
        [
            "~~~~~~~~~~~~~~~~~~~~~~~~",
            "Textulator Version 1.0.0",
            "    Created by Tfff1    ",
            "~~~~~~~~~~~~~~~~~~~~~~~~",
            "For help, type 'help', to exit type 'exit', use 'clear' to clear the console."
        ],
        [
            "\n",
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
            "Welcome to the Textulator Help!",
            "Here's some basic, starter information:",
            "This calculator using the Python sytax (it's pretty standard):",
            "* is used for multiplication",
            "/ is used for division",
            "+ is used for addition",
            "- is used for subtraction",
            "** is used for exponential calculations (powers)",
            "% is used to find the remainder of a division",
            "// is used for floor division (everything after the decimal point is removed), shorthand for: floor(x / y)",
            "For more detailed help go to: https://docs.python.org/3/library/math.html (remove the math. from the start though)",
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
            "PLEASE NOTE: Some functions may, or may not be available depending on which version of Python you are using. The more recent, the better."
        ]
    ]
def printStart():
    for line in info[0]:
        print(line)

printStart()

Ans = 0
n = ""
while n != "exit" and n != "close" and n != "'exit'" and n != "'close'":
    n = uInput(">> ")
    if n != "exit" and n != "close" and n != "help" and n != "'exit'" and n != "'close'" and n != "'help'" and n != "clear" and n != "'clear'":
        try:
            print(eval(n))
            Ans = eval(n)
        except:
            print("There's something wrong with that last equation you entered.")
    elif n == "help" or n == "'help'":
        for line in info[1]:
            print(line)
    elif n == "clear" or n == "'clear'":
        os.system('cls' if os.name == 'nt' else 'clear')
        printStart()