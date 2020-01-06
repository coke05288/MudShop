from view import *
from model.model_get_items import *
from control.control_buy_items import *

view_user = ViewUser()
view_type = ViewType()

# def get_category():
#     view_user.print_get_category()

def get_all_items():

    command_admin = {
        1 : buy_items,
        2 : "back",
        # 3 : edit_items,
        # 4 : get_sales
    }

    while True:
        view_user.print_get_all_items()

        command_input = input()
        if command_input == "1":
            int(command_input)
            try:
                command_admin[command_input]()
            except KeyError:
                print("잘못입력하셨습니다!")
                continue 
        elif command_input == "2":
            return
        else:
            continue
            
    
def get_bill():
    view_user.print_get_bill()
