from django.test import TestCase
from django.core.urlresolvers import reverse

class ConverterTests(TestCase):
    def test_check_media_without_id(self):
        data = {}
        response = self.client.get(reverse('check_media'), data)
        self.assertContains(response, 'Passe o media_id')
    def test_check_media_wrong_id(self):
        data = {'media_id': "22"}
        response = self.client.get(reverse('check_media'), data)
        self.assertContains(response, 'incorreto')


