#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from selenium import webdriver
import os, platform, sys
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)

from features.utils.util import generate_report

def before_scenario(context, scenario):
    language = context.config.userdata['language']
    if (language == "pt"):
        browser_language = {'intl.accept_languages': 'pt,pt_BR'}
    elif (language == "es"):
        browser_language = {'intl.accept_languages': 'es,es_LA'}
    else:
        browser_language = {'intl.accept_languages': 'en,en_US'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', browser_language)
    if platform.system() == 'Darwin':
        context.driver = webdriver.Chrome(executable_path=os.path.dirname(os.path.realpath(__file__)) + "/resources/chromedriver", chrome_options=options)
    elif platform.system() == 'Windows':
        context.driver = webdriver.Chrome(executable_path=os.path.dirname(os.path.realpath(__file__)) + "/resources/chromedriver.exe", chrome_options=options)
    context.driver.implicitly_wait(15)
    context.driver.delete_all_cookies()
    context.driver.maximize_window()

def after_scenario(context, scenario):
    context.driver.quit()