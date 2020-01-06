from view import *
from control.control_admin_command import*
from control.control_user_command import*

view_admin = ViewAdmin()
view_user = ViewUser()
view_type = ViewType()

def select_admin_command():
    
    command_input = ''

    command_admin = {
        1 : get_items,
        2 : add_items
        # 3 : edit_items,
        # 4 : get_sales
        }

    while True:
        view_type.print_admin_home()
        try:
            command_input = str(input())
            
            if command_input == "Back":
                return
            else:
                int(command_input)
                print("Test")
                command_admin[command_input]()
        except Exception:
            print("잘못입력하셨습니다!")
            continue    

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
            print("잘못입력하셨습니다!")
            continue
        else:
            break