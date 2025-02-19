from locators.locators import NAME_FIELD, EMAIL_FIELD, SEND_BUTTON, START_BUTTON, WRONG_EMAIL_MSG, EMODJI_BUTTON, \
    SMILE_EMODJI, TEXT_AREA, HELLO_TEXT, USER_DATA_PANEl
from pages.base_page import BasePage


class ChatPage(BasePage):

    PAGE_URL = "https://autofaq.ai/"

    def start_button(self):
        return self.find(START_BUTTON)

    def name_field(self):
        return self.find(NAME_FIELD)

    def email_field(self):
        return self.find(EMAIL_FIELD)

    def send_button(self):
        return self.find(SEND_BUTTON)

    def wrong_email_message(self):
        return self.find(WRONG_EMAIL_MSG)

    def emodji_button(self):
        return self.find(EMODJI_BUTTON)

    def smiling_emodji(self):
        return self.find(SMILE_EMODJI)

    def text_area(self):
        return self.find(TEXT_AREA)

    def hello_text(self):
        return self.page.get_by_text(HELLO_TEXT)

    def user_data_panel(self):
        return self.find(USER_DATA_PANEl)