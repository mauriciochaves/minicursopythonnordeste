import os
import sys
from appium import webdriver
from datetime import datetime
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)
from util.utils import generate_report

def before_all(context):
    desired_caps = {}
    desired_caps['platformName']='Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['appPackage'] = "com.android.chrome"
    desired_caps['appActivity'] = "com.google.android.apps.chrome.Main"
    desired_caps['appWaitDuration'] = '30000' # tempo limite em milisegundos para aguardar o lançamento de uma activity
    desired_caps['deviceReadyTimeout'] = '30' # tempo limite em segundos para aguardar o device ficar pronto
    desired_caps['androidDeviceReadyTimeout'] = '30' # tempo limite em segundos usado para aguardar que o dispositivo fique pronto após a inicialização
    desired_caps['autoWebviewTimeout'] = '30000' # tempo limite em milisegundos usado para aguardar que o context webview se torne ativo
    desired_caps['appWaitActivity'] = 'com.android.chrome, com.google.android.apps.chrome.Main' # aguarda determinadas Activitys carregarem, importante setar a Activity de Login para não quebrar de um scenario para outro
    # desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'apks/(name_apk)'))
    
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    with open("time.txt", "a") as f:
        print("Execution Start: "+str(datetime.now()), file=f)


def before_feature(context, feature):
    with open("time.txt", "a") as f:
        print(context.feature.name, file=f)
        print("Feature Execution Start: "+str(datetime.now()), file=f)


def before_scenario(context, scenario):
    with open("scenarios.txt", "a") as f:
        print(context.scenario.name, file=f)


def after_scenario(context, scenario):
    context.driver.start_activity("com.android.chrome", "com.google.android.apps.chrome.Main")
    with open("scenarios.txt", "a") as f:
        print(context.scenario.name, file=f)


def after_feature(context, feature):
    with open("time.txt", "a") as f:
        print("Feature Execution End: "+str(datetime.now()), file=f)


def after_all(context):
    generate_report(context.config.userdata['SYSTEM'])
    with open("time.txt", "a") as f:
        print("Execution End: "+str(datetime.now()), file=f)