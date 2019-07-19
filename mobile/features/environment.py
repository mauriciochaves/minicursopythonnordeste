import os
import sys
from appium import webdriver
from datetime import datetime
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)


def before_all(context):
    desired_caps = {}
    desired_caps['platformName']='Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = 'Android'
    desired_caps['appWaitDuration'] = '30000' # tempo limite em milisegundos para aguardar o lançamento de uma activity
    desired_caps['deviceReadyTimeout'] = '30' # tempo limite em segundos para aguardar o device ficar pronto
    desired_caps['androidDeviceReadyTimeout'] = '30' # tempo limite em segundos usado para aguardar que o dispositivo fique pronto após a inicialização
    desired_caps['autoWebviewTimeout'] = '30000' # tempo limite em milisegundos usado para aguardar que o context webview se torne ativo
    desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'apks/CTAppium-1-1.apk'))
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    pass


def after_feature(context, feature):
    pass