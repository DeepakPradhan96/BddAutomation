from selenium.webdriver import Chrome
#context= global/use entair project

def before_all(context):
    path='C:\\Driver\\chromedriver_win32\\chromedriver.exe'
    context.driver =Chrome(executable_path=path)


def after_all(context):
# def after_feature(context,feature):
#def after_scenario(context,scenario):
#def after_tag,step(context,tag):
    context.driver.close()
