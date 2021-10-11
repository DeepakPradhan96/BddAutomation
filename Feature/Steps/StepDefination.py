import time

from behave import *
#from selenium.webdriver import Chrome#context

#context.driver=Chrome

@given(u'User is on Registation Page')
def step_impl(context):

    context.driver.get('https://thetestingworld.com/testings/')


@when(u'User Enter Username')
def step_impl(context):
    context.driver.find_element_by_name('fld_username').send_keys('deep')

@when(u'User Enter Email id')
def step_impl(context):
    context.driver.find_element_by_name('fld_email').send_keys('dep@123')


@when(u'User Enter Password')
def step_impl(context):
    context.driver.find_element_by_name('fld_password').send_keys('1234')
    time.sleep(2)


@when(u'User Click on Signup Button')
def step_impl(context):
    context.driver.find_element_by_xpath('//input[@type="submit"]').click()


@then(u'User Should be Register Successfully')
def step_impl(context):
    print('STEP: Then User Should be Register Successfully')



@when(u'User Enter Dupilicate Username')
def step_impl(context):
     print('ok')


#behave --tags=smoke,sanaty(or)
# behave --tags=smoke --tags=sanaty(and)

