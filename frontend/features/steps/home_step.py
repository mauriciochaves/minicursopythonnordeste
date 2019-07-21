#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from behave import *
from features.pages.home_page import HomePage

use_step_matcher("re")


@given("I open: https://en.wiktionary.org/prepare by the first time")
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.navigate_page(context.config.userdata['url'])

@when("I am on homepage")
def step_impl(context):
    context.home_page.assertPage()

@then("I type on look up search text: (?P<searchTxt>.+)")
def step_impl(context, searchTxt):
    context.home_page.type_lookUp(searchTxt)

@then("I click on lookup search button")
def step_impl(context, searchTxt):
    context.home_page.click_lookUpSearch()

@then("I look up the definition of the word (?P<searchTxt>.+)")
def step_impl(context, searchTxt):
    context.home_page.realize_search(searchTxt)