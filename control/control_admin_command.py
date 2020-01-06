from view import *
from model.model_add_items import *
from model.model_get_items import *

view_admin = ViewAdmin()
view_type = ViewType()

def get_items():
    view_admin.print_get_items()
    exec_get_items()
    while True:
        try:
            command_data = input("뒤로가기는 'Back'을 입력해주세요")
            if command_data == "Back":
                return
            else:
                continue
        except Exception:
            print("잘못입력하셨습니다!")   

def add_items():
    view_admin.print_add_items()

    item_data =[]

    try:
        item_data = input('등록할 상품 정보를 입력해 주세요(,로 구분해주세요) : ').split(',')
        if item_data == "Back":
            return
        else:
            exec_add_items(item_data)
    except Exception:
        print("잘못입력하셨습니다!")        

    while True:
        continue_command = input('추가 등록(Yes), 뒤로가기(No) : ')
        if continue_command == 'Yes':
            try:
                item_data = input('등록할 상품 정보를 입력해 주세요(,로 구분해주세요) : ').split(',')
                exec_add_items(item_data)
            except Exception:
                print("잘못입력하셨습니다!")
                continue                

        elif continue_command == 'No':
            return
        else:
            continue
    
    
# def edit_items():
#     view_admin.print_edit_items()

# def get_sales():
#     view_admin.print_get_sales()