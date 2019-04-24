import unittest
from appium import webdriver

class Driver_appium():

    def __init__(self, local_appium):
        
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['deviceName'] = 'ce011711dcd5671c05'
        #desired_caps['browserName'] = 'Chrome'
        desired_caps['appPackage'] = 'com.instagram.android'
        desired_caps['appActivity'] = 'com.instagram.android.activity.MainTabActivity'
        #desired_caps['app'] = 'com.instagram.android/.activity.MainTabActivity,android.intent.action.MAIN,NULL,NULL,270532608,com.sec.android.app.launcher'
        self.driver = webdriver.Remote(local_appium, desired_caps)

    def get_driver(self):
        return self.driver

