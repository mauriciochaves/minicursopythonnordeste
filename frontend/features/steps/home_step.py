#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from behave import *
from features.pages.home_page import HomePage

use_step_matcher("re")


@given("texte de steps abrindo pagina")
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.navigate_page(context.config.userdata['url'])

@then("exemplo basico")
def step_impl(context, searchTxt):
    context.home_page.type_lookUp(searchTxt)