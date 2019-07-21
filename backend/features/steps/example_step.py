import requests
from hamcrest import assert_that, is_

@given(u'I create the users')
def step_impl(context):
    for row in context.table:
        data = {
        "name": row['name'],
        "job": row['job']
        }
        context.response = requests.post(context.base_url + "users", data)


@when(u'I list user with id {user_id}')
def step_impl(context, user_id):
    context.response = requests.get(context.base_url + "users/" + user_id)


@when(u'I list users with page "{page}"')
def step_impl(context, page):
    context.response = requests.get(context.base_url + "users?page=" + page)


@then(u'I verify status code {status_code}')
def step_impl(context, status_code):
    assert_that(context.response.status_code, is_(int(status_code)))