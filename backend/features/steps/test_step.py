import json
import requests
from behave import given, when, then, step
from hamcrest import assert_that, is_
import backend.features.common.request_generic as rq


@given(u'Eu efetuo requisição "{metodo}" para "{endpoint}" com identificação usuário "{id}"')
def get_url_method_data(context, metodo, endpoint, id):
    context.endpont_final = context.base_url + endpoint + id
    headers = {'Content-Type' : 'application/json'}
    context.response = rq.send_request_generic(context.endpont_final, metodo, headers)
    context.status_code = context.response.status_code
    context.result = context.response.json()
     
    
@then(u'Eu verifico o codigo de retorno "{codigo_retorno}"')
def step_impl(context, codigo_retorno):
    assert_that(int(context.status_code), is_(int(codigo_retorno)))

@then(u'Eu verifico o campo primeiro nome "{primeiro_nome}"')
def step_impl(context, primeiro_nome):
    assert_that(context.result["data"]["first_name"], is_(primeiro_nome))

@then(u'Eu verifico o campo ultimo nome "{ultimo_nome}"')
def step_impl(context, ultimo_nome):
    assert_that(context.result["data"]["last_name"], is_(ultimo_nome))

@then(u'Eu verifico o campo avatar "{avatar}"')
def step_impl(context, avatar):
    assert_that(context.result["data"]["avatar"], is_(avatar))     

@then(u'Eu verifico o campo email "{email}"')
def step_impl(context, email):
    assert_that(context.result["data"]["email"], is_(email))

@given(u'Eu efetuo solicitação de dados do usuario')
def get_url_method_data_context_table(context):
    for row in context.table:
        context.endpont_final = context.base_url + row["endpoint"] + row["id"]
        headers = {'Content-Type' : 'application/json'}
        context.response = rq.send_request_generic(context.endpont_final, row["metodo"], headers)
        context.status_code = context.response.status_code
        context.result = context.response.json()     

@then(u'Eu verifico seu retorno da solicitação')
def step_impl(context):
    for row in context.table:
        assert_that(int(context.status_code), is_(int(row["codigo_retorno"])))
        assert_that(context.result["data"]["first_name"], is_(row["primeiro_nome"]))
        assert_that(context.result["data"]["last_name"], is_(row["ultimo_nome"]))
        assert_that(context.result["data"]["avatar"], is_(row["avatar"]))
        assert_that(context.result["data"]["email"], is_(row["email"]))