class ViewType:

    def print_intro(self,):
        print("Welcome to the fantastic Mud Shopping Mall, MADMUDSHOP!!")
        print("(Select your member type.)")

    def print_admin_home(self,):
        print()
        print("-----------------------------------")
        print()
        print("Here is Administrator Page")

        print("(Choose you will action)")
        print("1. 상품 조회 \t 2. 상품 등록 \t 3. 상품 수정 \t 4. 매출 조회")

    def print_user_home(self,):
        print()
        print("-----------------------------------")
        print()
        print("Here is User Page")

        print("(Choose you will action)")
        print("1. 상품 카테고리 조회 \t 2. 상품 전체 조회 \t 3. 주문 내역 조회")

class ViewAdmin:

    def get_items(self,):
        print("get_items")
    def add_items(self,):
        print("add_items")
    def edit_items(self,):
        print("edit_items")
    def get_sales(self,):
        print("get_sales")

        

class ViewUser:

    def get_category(self,):
        print("get_category")
    def get_all_items(self,):
        print("get_all_items")
    def get_bill(self,):
        print("get_bill")




    