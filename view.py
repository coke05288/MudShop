class ViewType:

    def print_intro(self,):
        print("반갑습니다. 세상 맛있는 돈까스 쇼핑몰, 돈까트립에 오신 것을 환영합니다!")
        print("(회원 타입을 선택해주세요.)")

    def print_admin_home(self,):
        print()
        print("-----------------------------------")
        print()
        print("이곳은 관리자 페이지 입니다.")

        print("(행동을 선택해주세요)")
        # print("1. 상품 조회 \t 2. 상품 등록 \t 3. 상품 수정 \t 4. 매출 조회")
        print("1. 상품 조회 \t 2. 상품 등록")

    def print_user_home(self,):
        print()
        print("-----------------------------------")
        print()
        print("이곳은 유저 페이지 입니다.")

        print("(행동을 선택해주세요)")
        # print("1. 상품 카테고리 조회 \t 2. 상품 전체 조회 \t 3. 주문 내역 조회")
        print("1. 상품 구매 \t 2. 주문 내역 조회")

class ViewAdmin:

    def print_get_items(self,):
        print()
        print("-----------------------------------")
        print()
        print("상품 전체 리스트입니다!")

    def print_add_items(self,):
        print()
        print("-----------------------------------")
        print()
        print("상품 등록 페이지 입니다!")
        print("(상품id, 상품이름, 상품가격, 상품수량 순으로 입력해주세요)")

    # def print_edit_items(self,):
    #     print()
    #     print("-----------------------------------")
    #     print()
    #     print("You can edit your registered product here!")
    #     print("(상품 수정 뷰)")

    # def print_get_sales(self,):
    #     print()
    #     print("-----------------------------------")
    #     print()
    #     print("You can check your sales here!")
    #     print("(매출 뷰)")

        

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
        print("상품 구매 페이지입니다.")
        print("(전체 상품 리스트 뷰)")

    def print_get_bill(self,):
        print()
        print("-----------------------------------")
        print()
        print("아래는 주문내역 리스트 입니다.")
        print("(주문내역 리스트)")




    