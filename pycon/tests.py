from unittest.mock import patch
from django.shortcuts import reverse
from django.test import TestCase, Client
from pycon.utils import display, demo



class PyconViewTest(TestCase):

    def test_template_used(self):
        response = self.client.get(reverse('pycon:welcome'))
        self.assertTemplateUsed('pycon.html')

    def test_response_returned(self):
        response = self.client.get(reverse('pycon:welcome'))
        self.assertEqual(response.status_code, 200)


class TestDisplay(TestCase):

    @patch('pycon.utils.Screen.wrapper')
    def test_display(self, screen):
        """ Test that display function is called when demo is executed """
        demo()
        screen.assert_called_with(display)
