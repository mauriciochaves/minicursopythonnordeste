from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class ExamplePage(BasePage):
    form_option = (By.XPATH, "//a[.='Formulário']")
    name_text = (By.ID, "nome")
    date_checkbox = (By.ID, "check")
    hour_switch = (By.ID, "switch")
    save_button = (By.XPATH,"//a[.='SALVAR']")


    def click_on_form_option(self):
        super().click(self.form_option)


    def click_on_date_checkbox(self):
        super().click(self.date_checkbox)


    def click_on_hour_switch(self):
        super().click(self.hour_switch)


    def click_on_save_button(self):
        super().click(self.save_button)


    def set_name_text(self, text):
        super().type_in(self.name_text, text)