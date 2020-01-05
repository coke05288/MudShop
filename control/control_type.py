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
        print("1. 관리자 \t 2. 유저 ")
        type_input = int(input())
        try:
            command_type[type_input]()
        except KeyError:
            print("잘못입력하셨습니다!")
            continue
        else:
            break
        

    print()