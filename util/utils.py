import json
import requests
import os


def get(url, token, **param):
    header = generate_header() if token == None else generate_header(content_type='application/json', token=token)
    url = generate_url_with_param(url, param)

    try:
        response = requests.get(url, headers=header)
        return response
    except OSError as err:
        print_exception("request GET failed:", err, response)


def post(url, token = None, data = {}, content_type = 'application/json'):
    header = generate_header() if token == None else generate_header(content_type=content_type, token=token)

    try:
        response = requests.post(url, data=json.dumps(data), headers=header)
        return response
    except OSError as err:
        print_exception("request POST failed:", err, response)
    except AttributeError as error:
        print("\n >>'header' can bot be 'str'<<" + "\n\nfunction name: " + post.__name__ + "\nmessage: " + str(error))


def put(url, token, data, content_type = 'application/json'):
    header = generate_header() if token == None else generate_header(content_type=content_type, token=token)

    try:
        response = requests.put(url, data=json.dumps(data), headers=header)
        return response
    except OSError as err:
        print_exception("request PUT failed:", err, response)
    except AttributeError as error:
        print("\n >>'header' can bot be 'str'<<" + "\n\nfunction name: " + post.__name__ + "\nmessage: " + str(error))


def delete(url, token):
    header = generate_header() if token == None else generate_header(content_type='application/json', token=token)

    try:
        response = requests.delete(url, headers=header)
        return response
    except OSError as err:
        print_exception("request DELETE failed:", err, response)
    except AttributeError as error:
        print("\n >>'header' can bot be 'str'<<" + "\n\nfunction name: " + post.__name__ + "\nmessage: " + str(error))


def print_exception(function_name, error, response):
    print("request: " + function_name + " - status_code: " + str(response.status_code) + " - message: " + response.text)
    print("\n\n")
    print(">>>>>" + function_name + str(error))


def generate_data_file(**data):
    return data


def generate_header(**header):
    if header != {}:
        header['content-type'] = header.pop('content_type')
    else:
        header = generate_header(content_type='application/json')
    return header


def generate_url_with_param(url, param):
    if param is not None:	
        for index, key in enumerate(param):
            if index == 0:
                url = url + '?' + str(key) + '=' + str(param[key])
            else:
                url = url + '&' + str(key) + '=' + str(param[key])
    return url


def generate_report(system):
    if system.lower() == 'win':
        os.system("powershell.exe -Command '& allure generate allure-results --clean -o allure-html'")
        os.system("ren allure-html' allure-html")
        os.system('start microsoft-edge: file:///C:/Projetos/Pessoais/python_workspace/backend/allure-html/index.html')

    elif system.lower() == 'linux':
        os.system("allure generate allure-results --clean -o allure-html")