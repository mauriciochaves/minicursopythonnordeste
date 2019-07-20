#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from selenium import webdriver
import os, platform, sys

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    if platform.system() == 'Darwin':
        context.driver = webdriver.Chrome(executable_path=os.path.dirname(os.path.realpath(__file__)) + "/resources/chromedriver", chrome_options=options)
    elif platform.system() == 'Windows':
        context.driver = webdriver.Chrome(executable_path=os.path.dirname(os.path.realpath(__file__)) + "/resources/chromedriver.exe", chrome_options=options)
    context.driver.implicitly_wait(15)
    context.driver.delete_all_cookies()
    context.driver.maximize_window()

def after_scenario(context, scenario):
    context.driver.quit()