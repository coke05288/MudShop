from view import *
from model.model_buy_items import *

view_user = ViewUser()

def buy_items():
    view_user.print_buy_items()

    order_data = input().split(',')

    buy_item_id = order_data[0]
    buy_item_quntity = order_data[1]

    exec_buy_items(buy_item_id, buy_item_quntity)