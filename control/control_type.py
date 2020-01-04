from view import ViewType
from control.control_list_command import *

view_intro = ViewType()

def select_type():

    type_input = 0

    command_type = {
    1 : select_admin_command,
    2 : select_user_command
    }
    
    view_intro.print_intro()

    while True:
        print("1. Administrator \t 2. User ")
        type_input = int(input())
        try:
            command_type[type_input]()
        except KeyError:
            print("You mistyped it!")
            continue
        else:
            break
        

    print()