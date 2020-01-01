# class ViewAdmin:

#     command_input = 0

#     command_admin = {
#         1 : get_items,
#         2 : add_items,
#         3 : edit_items,
#         4 : get_sales
#         }

#     def print_admin_home(self,):
#         print()
#         print("-----------------------------------")
#         print()
#         print("관리자 홈입니다.")
#         print("(회원님의 회원 유형을 선택해 주세요.)")
#         print("1. 상품 조회 \t 2. 상품 등록 \t 3. 상품 수정 \t 4. 매출 조회")

#     def get_items(self,):
#         print("get_items")
#     def add_items(self,):
#         print("add_items")
#     def edit_items(self,):
#         print("edit_items")
#     def get_sales(self,):
#         print("get_sales")
    
#     def input_command(self,):
#         command_input = int(input())
#         try:
#             ViewAdmin.command_admin[command_input]()
#         except KeyError:
#             print("잘못 입력하셨습니다!")
        
        
def print_admin_home():
    print()
    print("-----------------------------------")
    print()
    print("Here is Administrator Page")

    print("(Choose you will action)")
    print("1. 상품 조회 \t 2. 상품 등록 \t 3. 상품 수정 \t 4. 매출 조회")

def print_user_home():
    print()
    print("-----------------------------------")
    print()
    print("Here is User Page")

    print("(Choose you will action)")
    print("1. 상품 조회 \t 2. 상품 등록 \t 3. 상품 수정 \t 4. 매출 조회")
    