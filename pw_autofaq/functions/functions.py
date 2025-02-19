from pages.chat_page import ChatPage

def start_chat(page):
    chat_page = ChatPage(page)
    chat_page.start_button().click()

def enter_name(page, name):
    chat_page = ChatPage(page)
    chat_page.name_field().click()
    chat_page.name_field().fill(name)

def enter_email(page, email):
    chat_page = ChatPage(page)
    chat_page.email_field().click()
    chat_page.email_field().fill(email)

def send_button_click(page):
    chat_page = ChatPage(page)
    chat_page.send_button().click()

def emodji_click(page):
    chat_page = ChatPage(page)
    chat_page.emodji_button().click()

def smiling_emodji_select(page):
    chat_page = ChatPage(page)
    chat_page.smiling_emodji().click()

def text_area(page):
    chat_page = ChatPage(page)
    chat_page.text_area()