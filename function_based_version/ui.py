from function_based_version.utils import welcome_message, logout_message
def about_page():
    welcome_tab_choose = input(welcome_message)
    match welcome_tab_choose:
        case"2":
            pass
        case "0":
            print(logout_message)
