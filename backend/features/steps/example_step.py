import json
import requests
from behave import given, when, then, step
from behave import *
import backend.features.common.request_generic as rq


@given(u'Eu efetuo requisição "{metodo}" para "{endpoint}" com identificação usuário "{id}"')
def get_url_method_data(context, metodo, endpoint, id):
    context.endpont_final = context.base_url + endpoint + id
    context.response = rq.send_request_generic(context.endpont_final)
    print(context.response)




# @given('I submit POST request on url "(?P<url>.+)" using: "(?P<email>.+)" value to "email" field, "(?P<password>.+)" value to "password" field')
# def step_impl(context, url, email, password):
#     payload = {'email': email, 'password': password}
#     context.response = requests.post(BASE_URL + url, json=payload)


# @when("I check result response")
# def step_impl(context):
#     context.status_code = context.response.status_code
#     context.data = context.response.json()


# @then("I check status code (?P<status_code>.+)")
# def step_impl(context, status_code):
#     assert (int(context.status_code) == int(status_code))


# @step('I check the field "(?P<field>.+)" containing the not empty value')
# def step_impl(context, field):
#     assert (field in context.data)
#     assert (context.data[field] != "")


# @given('I submit POST request on url "(?P<url>.+)" using: "(?P<email>.+)" value to "email" field')
# def step_impl(context, url, email):
#     payload = {'email': email}
#     context.response = requests.post(BASE_URL + url, json=payload)


# @step('I check the field "(?P<field>.+)" containing the value "(?P<field_value>.+)"')
# def step_impl(context, field, field_value):
#     assert (field in context.data)
#     assert (context.data[field] == field_value)


# @given('I submit POST request on url "(?P<url>.+)" using: "(?P<name>.+)" value to "name" field, "(?P<job>.+)" value to "job" field')
# def step_impl(context, url, name, job):
#     payload = {'name': name, 'job': job}
#     context.response = requests.post(BASE_URL + url, json=payload)


# @step('I check value of the parameter "(?P<param>.+)" from results response')
# def step_impl(context, param):
#     context.param = context.response.json()[param]


# @when('I submit PUT request on url "(?P<url>.+)" using: "(?P<name>.+)" value to "name" field, "(?P<new_job>.+)" value to "job" field')
# def step_impl(context, url, name, new_job):
#     payload = {'name': name, 'job': new_job}
#     user_id = context.param
#     context.response = requests.put(BASE_URL + url + user_id, json=payload)


# @given('I submit GET request on url "(?P<url>.+)"')
# def step_impl(context, url):
#     context.response = requests.get(BASE_URL + url)


# @step('I check the field "(?P<field>.+)" containing the value "(?P<field_value>.+)" in "(?P<field_root>.+)" field')
# def step_impl(context, field, field_value, root_field):
#     assert (str(context.data[root_field][field]) == str(field_value))