import os
import sys
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)


def before_all(context):
    context.base_url = context.config.userdata['URL']
    print("before_all")

def before_feature(context, feature):
    print("before_feature")


def before_scenario(context, scenario):
    print("before_scenario")


def after_scenario(context, scenario):
    print("after_scenario")


def after_feature(context, feature):
    print("after_feature")


def after_all(context):
    print("after_all")