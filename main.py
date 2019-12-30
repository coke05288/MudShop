
import sqlite3
from view import*

type_input = 0

print("Welcome to the fantastic Mud Shopping Mall, MADMUDSHOP!!")
print("(Select your member type.)")

command = {
    1 : print_admin_home,
    2 : print_user_home
}

while True:
    print("1. Administrator \t 2. User ")
    type_input = int(input())
    try:
        command[type_input]()
    except KeyError:
        print("You mistyped it!")
        continue
    else:
        break
    

print()