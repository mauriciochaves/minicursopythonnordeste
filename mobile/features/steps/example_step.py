from hamcrest import assert_that, equal_to
from pages.example_page import ExamplePage


@given(u'Eu inicio a aplicação')
def step_impl(context):
    context.page = ExamplePage(context.driver)


@given(u'Eu clico na opção formulário')
def step_impl(context):
    context.page.click_on_form_option()


@when(u'Eu preencho o formulário com os dados abaixo')
def step_impl(context):
    for row in context.table:
        context.page.set_name_text(row['name'])
        context.page.set_date_checkbox(row['checkbox'])
        context.page.set_hour_switch(row['switch'])
        context.page.click_on_save_button()