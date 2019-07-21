from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def refresh(self):
        self.driver.refresh()

    def open_url(self, url):
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def click(self, locator):
        self.wait_for(EC.element_to_be_clickable(locator)).click()

    def find(self, locator):
        element = self.wait_for(EC.visibility_of_element_located(locator))
        return element

    def elements_by_class(self, locator):
        return self.driver.find_elements_by_class_name(locator)

    def wait_for(self, condition, seconds=30):
        return WebDriverWait(self.driver, seconds).until(condition)

    def type_in(self, locator, text, set_clear=True):
        element = self.find(locator)
        if set_clear:
            element.clear()
        element.send_keys(text)

    def type_in_by_id(self, id, text, set_clear=True):
        element = self.driver.find_elements_by_id(id)[0]
        if set_clear:
            element.clear()
        element.send_keys(text)

    def wait(self, time):
        return WebDriverWait(self.driver, time)

    def type_with_javascript_by_class_name(self, class_name, index, text):
        self.driver.execute_script('document.getElementsByClassName("' + class_name + '")[' + index + '].innerHTML = "' + text + '";')

    def type_with_javascript(self, id, index, text):
        self.driver.execute_script('document.getElementsByID("' + id + '")[' + index + '].innerHTML = "' + text + '";')

    def select_in_combo_visible_text(self, locator, value):
        Select(self.wait_for(EC.visibility_of_element_visible(locator))).select_by_value(value)

    def select_in_combo_by_index(self, locator, value):
        element = Select(self.driver.find_element_by_id(locator[1]))
        element.select_by_index(value)

    def select_in_combo_by_value2(self,locator, value):
        element = Select(self.driver.find_element_by_id(locator[1]))
        element.select_by_value(value)

    def select_in_combo_by_text(self,locator, value):
        element = Select(self.driver.find_element_by_id(locator[1]))
        element.select_by_visible_text(value)

    def select_in_combo_visible_by_index(self, locator, value):
        Select(self.wait_for(EC.visibility_of_element_located(locator))).select_by_index(value)

    def select_in_combo_by_xpath(self, locator, content):
        self.click(locator)
        path = "//div[@value="+"'"+content+"'"+"]"
        item = self.driver.find_elements_by_xpath(path)
        item[0].click()

    def find_by_id(self, id):
        z = id[1]
        element = self.driver.find_elements_by_id(z)
        print(element.text())
        return element
    
    def find_by_xpath(self, locator):
        z = locator[1]
        element = self.driver.find_elements_by_xpath(z)
        return element

    def find_by_css(self, css):
        z = css[1]
        element = self.driver.find_elements_by_css_selector(z)
        return element

    def return_elements_on_cell(self, expected):
        baseTable = self.driver.find_elements_by_xpath('//*[@class="item"]/div')
        for item in baseTable:
            time.sleep(8)
            if item.text == expected:
                return item

    def return_text(self, locator):
        return self.find(locator).text

    def return_value(self, locator):
        return self.find(locator).get_attribute('value')

    def press_down(self, locator):
        self.find(locator).send_keys(Keys.ARROW_DOWN)

    def press_enter(self, locator):
        self.find(locator).send_keys(Keys.RETURN)

    def press_back_space(self, locator):
        self.find(locator).send_keys(Keys.BACK_SPACE)

    def elements_by_class_wait(self, locator, index):
        elements = self.elements_by_class(locator)
        return self.wait_for(EC.visibility_of(elements[index]))

    def switch_tab(self, index):
        self.driver.switch_to_window(self.driver.window_handles[index])

