from view import *

view_admin = ViewAdmin()
view_user = ViewUser()
view_type = ViewType()

def select_admin_command():
    
    command_input = 0

    command_admin = {
        1 : view_admin.get_items,
        2 : view_admin.add_items,
        3 : view_admin.edit_items,
        4 : view_admin.get_sales
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
        1 : view_user.get_category,
        2 : view_user.get_all_items,
        3 : view_user.get_bill
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