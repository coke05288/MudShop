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
        # print("1. 상품 카테고리 조회 \t 2. 상품 전체 조회 \t 3. 주문 내역 조회")
        print("1. 상품 전체 조회 \t 2. 주문 내역 조회")

class ViewAdmin:

    def print_get_items(self,):
        print()
        print("-----------------------------------")
        print()
        print("You can look up your product here!")
        print("(상품 전체 리스트)")

    def print_add_items(self,):
        print()
        print("-----------------------------------")
        print()
        print("You can register your product here!")
        print("(상품 등록 뷰)")

    def print_edit_items(self,):
        print()
        print("-----------------------------------")
        print()
        print("You can edit your registered product here!")
        print("(상품 수정 뷰)")

    def print_get_sales(self,):
        print()
        print("-----------------------------------")
        print()
        print("You can check your sales here!")
        print("(매출 뷰)")

        

class ViewUser:

    # def print_get_category(self,):
    #     print()
    #     print("-----------------------------------")
    #     print()
    #     print("Check out our product categories")
    #     print("(카테고리 뷰)")

    def print_get_all_items(self,):
        print()
        print("-----------------------------------")
        print()
        print("Check out full list of our products")
        print("(전체 상품 리스트 뷰)")

    def print_get_bill(self,):
        print()
        print("-----------------------------------")
        print()
        print("Below is your order history")
        print("(주문내역 리스트)")




    