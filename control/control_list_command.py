from view import *
from control.control_admin_command import*
from control.control_user_command import*

view_admin = ViewAdmin()
view_user = ViewUser()
view_type = ViewType()

def select_admin_command():
    
    command_input = 0

    command_admin = {
        1 : get_items,
        2 : add_items,
        3 : edit_items,
        4 : get_sales
        }

    view_type.print_admin_home()
    
    while True:
        command_input = int(input())
        try:
            command_admin[command_input]()
        except KeyError:
            print("You mistyped it!")
            continue
        else:
            break

def select_user_command():
     
    command_input = 0

    command_user = {
        # 1 : get_category,
        1 : get_all_items,
        2 : get_bill
        }

    view_type.print_user_home()

    while True:
        command_input = int(input())
        try:
            command_user[command_input]()
        except KeyError:
            print("You mistyped it!")
            continue
        else:
            break