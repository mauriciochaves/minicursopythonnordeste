#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class HomePage(BasePage):
    txtLookUp = (By.XPATH, ".//*[@class='mw-ui-input mw-ui-input-inline']")
    btnLookUpGo = (By.CLASS_NAME, "mw-ui-button")

    def navigate_page(self, url):
        self.open_url(url)

    def assertPage(self):
        assert self.get_title() == 'Wiktionary, the free dictionary'

    def type_lookUp(self, searchTxt):
        self.type_in(self.txtLookUp, searchTxt)
    
    def click_lookUpSearch(self):
        self.click(self.btnLookUpGo)

    def realize_search(self, searchTxt):
        self.type_in(self.txtLookUp, searchTxt)
        self.click(self.btnLookUpGo)