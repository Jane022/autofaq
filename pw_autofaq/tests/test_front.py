import allure
from playwright.sync_api import expect
import pytest
from functions.functions import enter_name, start_chat, send_button_click, emodji_click, smiling_emodji_select, enter_email
from pages.chat_page import ChatPage


class TestChat:

    @allure.story("Проверка обязательного поля имени")
    def test_name_field_is_required(self, page, name):
        chat_page = ChatPage(page)
        chat_page.open()
        start_chat(page)
        enter_name(page, name)
        send_button_click(page)
        expect(chat_page.wrong_email_message()).to_have_text("Требуется указать почту.")

    @allure.story("Проверка работы панели эмодзи")
    def test_emodji_panel_works_fine(self, page):
        chat_page = ChatPage(page)
        chat_page.open()
        start_chat(page)
        emodji_click(page)
        smiling_emodji_select(page)
        expect(chat_page.text_area()).to_have_text('😀')

    @allure.story("Проверка открытия панели чата")
    def test_chat_panel_opens_failing(self, page):
        chat_page = ChatPage(page)
        chat_page.open()
        start_chat(page)
        expect(chat_page.hello_text()).to_have_text("Здравствуйте. Представьтесь, пожалуйста.")


    @pytest.mark.parametrize("email", [
        "@mail.ru",
        "invalid-email",
        "user@.com",
    ])
    @allure.story("Проверка негативных сценариев для поля email")
    def test_email_field_negative(self, page, email, name):
        chat_page = ChatPage(page)
        chat_page.open()
        start_chat(page)
        enter_name(page, name)
        enter_email(page, email)
        send_button_click(page)
        expect(chat_page.wrong_email_message()).to_contain_text("Почта имеет неверный формат")

    @allure.story("Проверка успешной отправки пользовательских данных")
    def test_user_data_send_positive(self, page, name, email):
        chat_page = ChatPage(page)
        chat_page.open()
        start_chat(page)
        enter_name(page, name)
        enter_email(page, email)
        send_button_click(page)
        expect(chat_page.user_data_panel()).not_to_be_visible()