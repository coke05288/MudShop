from view import *
from model.model_add_items import *

view_admin = ViewAdmin()
view_type = ViewType()

def get_items():
    
    view_admin.print_get_items()

def add_items():
    view_admin.print_add_items()

    item_data =[]

    item_data = input('등록할 상품 정보를 입력해 주세요(,로 구분해주세요) : ').split(',')
    exec_add_items(item_data)

    while True:
        continue_command = input('추가 등록(Yes), 뒤로가기(No) : ')
        if continue_command == 'Yes':
            item_data = input('등록할 상품 정보를 입력해 주세요(,로 구분해주세요) : ').split(',')
            exec_add_items(item_data)

        elif continue_command == 'No':
            return
        else:
            continue
    
    

    
    
def edit_items():
    view_admin.print_edit_items()

def get_sales():
    view_admin.print_get_sales()