import requests

def send_request_generic(url, method, headers, body=None):
    try:    
        if method.upper() == "GET":
            response = requests.get(url,headers=headers, allow_redirects=False,verify=False)
        elif method.upper() == "POST":
            response = requests.post(url,headers=headers,json=body, allow_redirects=False,verify=False)
        elif method.upper() == "PUT":
            response = requests.put(url,headers=headers,data=body, allow_redirects=False,verify=False)
        elif method.upper() == "OPTIONS":
            response = requests.options(url,headers=headers, verify=False)
        return response

    except Exception as e:
       print("Exception from request_generic %s",e)
