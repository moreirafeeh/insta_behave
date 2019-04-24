from driver.driver import Driver_appium
from pages.instagram_page import instagram_page 

def before_all(context):
    context.driver = Driver_appium('http://localhost:4723/wd/hub')
    context.driver = context.driver.get_driver()
    context.instagram = instagram_page(context.driver)
    

def before_feature(context,feature):
    pass
	
def before_scenario(context,scenario):
	pass
def after_all(context):
    pass
def after_step(context, step):
    pass
def after_scenario(context, scenario):
    pass
