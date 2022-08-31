from django.test import Client
from django.test import TestCase
from rest_framework import status
from rest_framework.response import Response


from django.contrib.auth.models import User
from p1.models import *

class MainTestCase(TestCase):
    def setUp(self):
        c = Client()
        self.credentials = {
            'username': 'navid',
            'password': '12345'}
        new_user = User.objects.create_user(**self.credentials)
        self.user = new_user
        c.post('/api/rest-auth/login/', {'username': 'navid', 'password': '12345'})
        Test.objects.create(title='belbin', description='be',estimated_time=16)
        Questions.objects.create(Test= Test.objects.first(), Question_Text='Are you OK?')
        Options.objects.create(Question=Questions.objects.first(), Option_Text='option')


    def test_Response(self):
        client = Client()
        response1 = self.client.get(f'/api/total/')
        response2 = self.client.get(f'/api/answer/')
        response3 = self.client.get(f'/api/tests/')
        response4 = self.client.get(f'/api/questions/')
        response5 = self.client.get(f'/api/options/')
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)
        self.assertEqual(response4.status_code, 200)
        self.assertEqual(response5.status_code, 200)

    def test_loginpage(self):
        c = Client()
        response = c.post('/api/rest-auth/login/', {'username': 'navid', 'password': '12345'})
        self.assertEqual(response.status_code,200)


    def test_add_test(self):
        c = Client()
        response = c.post('/api/rest-auth/login/', {'username': 'navid', 'password': '12345'})
        self.assertEqual(response.status_code, 200)

        response2 = c.post('/api/tests/', {'title': 'Exam', 'description': 'Exam Test', 'estimated_time':16})
        self.assertEqual(response2.status_code, 201)
        self.assertEqual(Test.objects.all().count(), 2)
        response3 = c.post('/api/tests/', {'title': 'Exam2', 'description': 'Exam2 Test', 'estimated_time':14})
        self.assertEqual(response3.status_code, 201)
        self.assertEqual(Test.objects.all().count(), 3)


    def test_add_Question(self):
        c = Client()
        response = c.post('/api/rest-auth/login/', {'username': 'navid', 'password': '12345'})
        self.assertEqual(response.status_code, 200)

        response2 = c.post('/api/questions/', {'Test': 1, 'Question_Text': 'Are you OK?'})
        self.assertEqual(response2.status_code, 201)
        self.assertEqual(Questions.objects.all().count(),2)
        response3 = c.post('/api/questions/', {'Test': 1, 'Question_Text': 'How are you?'})
        self.assertEqual(response3.status_code, 201)
        self.assertEqual(Questions.objects.all().count(), 3)


    def test_add_option(self):
        c = Client()
        response = c.post('/api/rest-auth/login/', {'username': 'navid', 'password': '12345'})
        self.assertEqual(response.status_code, 200)

        response2 = c.post('/api/options/', {'Option_Text': 'option1', 'Question': 1})
        self.assertEqual(response2.status_code, 201)
        self.assertEqual(Options.objects.all().count(), 2)
        response3 = c.post('/api/options/', {'Option_Text': 'option2', 'Question': 1})
        self.assertEqual(response3.status_code, 201)
        self.assertEqual(Options.objects.all().count(), 3)

    def test_add_answer(self):
        c = Client()
        response = c.post('/api/rest-auth/login/', {'username': 'navid', 'password': '12345'})
        self.assertEqual(response.status_code, 200)

        response2 = c.post('/api/answer/', {'number': 3, 'Option': 1, 'user': 1})
        self.assertEqual(response2.status_code, 201)
        self.assertEqual(Answers.objects.all().count(), 1)
        response3 = c.post('/api/answer/', {'number': 6, 'Option': 1, 'user': 1})
        self.assertEqual(response3.status_code, 201)
        self.assertEqual(Answers.objects.all().count(), 2)