#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    myElementByID = (By.ID, "myElementID")
    myElementByXpath = (By.XPATH, "//*[@id='description']/div")

    def navigate_page(self, url):
        self.open_url(url)

    def assertPage(self):
        assert self.get_title() == 'my title page validation'

    def escrever_algo(self, searchTxt):
        self.type_in(self.txtLookUp, searchTxt)
    
    def clicar_emAlgo(self):
        self.click(self.btnLookUpGo)