from behave import *
from django.test import TestCase, Client
from django.http import HttpRequest




    
@when(u'user goes to home page')
def step(context):
    context.browser.get('https://minor-strawhatrobby.c9users.io/auth/login/')
        
@then(u'it should have the title \'Continuum\'')
def step_impl(context):
    print(context.browser.title)
    assert 'Continuum' == context.browser.title
    
@then(u'I enter username and password and click login')
def imp(context):
    c = Client()
    c.login(username='bpitMinor', password='in the93')
    
    cookie = c.cookies['sessionid']
    server_url = 'https://minor-strawhatrobby.c9users.io/auth/login/'
    b = context.browser
    b.get(server_url) # selenium will set cookie domain based on current page domain
    b.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
    
