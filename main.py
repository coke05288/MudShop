
import sqlite3
from view import*

type_input = 0

print("안녕하세요 머드 쇼핑몰 '매드머드숍' 입니다.")
print("(회원님의 회원 유형을 선택해 주세요.)")
print("1. 관리자 \t 2. 회원 ")

command = {
    1 : ViewAdmin.print_admin_home,
    2 : print_user_home
}

type_input = int(input())


try:
    command[type_input]()
except KeyError:
    print("잘못 입력하셨습니다!")
    

print()

# conn = sqlite3.connect ...
# c = conn.cursor()

## 상품과 주문 테이블을 생성하는 코드
# c.execute("CREATE TABLE ...

## 상품 데이터를 추가하는 코드
# c.execute("INSERT INTO ...

## 상품 목록을 표시하는 코드

# print('')
# print("구매하실 상품의 번호를 입력해주세요: ")


## 상품 번호와 주문 수량을 입력받는 코드
# print('')
# print("구매할 수량을 입력해주세요: ")


## 주문 데이터를 db에 추가하는 코드
# c.execute("INSERT INTO ...

## 현재까지 주문 내역을 출력하는 코드
# print('')
# print("현재까지 구매한 내역 보기")
# print('')