from view import *

view_admin = ViewAdmin()
view_type = ViewType()

def get_items():
    view_admin.print_get_items()

def add_items():
    view_admin.print_add_items()
    
def edit_items():
    view_admin.print_edit_items()

def get_sales():
    view_admin.print_get_sales()