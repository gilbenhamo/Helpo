# Create your tests here.
from django.test import TestCase
from home.models import QuestionAnswer

class TestModels(TestCase):
    def setUp(self):
        self.q_a_obj = QuestionAnswer.objects.create(
            Question = 'q',
            Answer = 'a'
        )
        
    def test_QuestionAnswer(self):
        self.assertEqual(self.q_a_obj.Question,'q')
        self.assertEqual(self.q_a_obj.Answer,'a')
        
        