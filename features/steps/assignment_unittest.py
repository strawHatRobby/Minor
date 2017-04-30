from behave import *
from django.test import TestCase, Client
from django.http import HttpRequest
from minor.views import home
from assignments.models import Assignment
from courses.models import Subject



@when(u'I go to create assignment page')
def step_impl(context):
    context.browser.get('https://minor-strawhatrobby.c9users.io/assignments/create_assignment/')
    

@then(u'I should be able to create an assignment')
def step_impl(context):
    assignment = Assignment.objects.create(title='test assignment', content='testing via behave BDD',marks=100,subject_id=Subject.objects.first())
    assignment.save()
    Assignment.objects.filter(title__startswith="test asssignment").delete()

@when(u'I go to list assignment page')
def step_impl(context):
    context.browser.get('https://minor-strawhatrobby.c9users.io/assignments/assignment_list/')

@then(u'assignment saved should be present')
def step_impl(context):
    assignment = Assignment.objects.create(title='test assignment 2', content='testing via behave BDD',marks=100,subject_id=Subject.objects.first())
    assignment.save()
    'test assignment 2' in Assignment.objects.filter(title__startswith="test asssignmen")
    Assignment.objects.filter(title__startswith="test assignment 2").delete()



