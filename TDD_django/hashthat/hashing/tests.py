import geckodriver_autoinstaller
from django.test import TestCase
from selenium import webdriver

from .forms import HashForm

geckodriver_autoinstaller.install()
"""
Check if the current version of geckodriver exists
and if it doesn't exist, download it automatically,
then add geckodriver to path
"""


class FunctionalTestCase(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_there_is_homepage(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Enter hash here:', self.browser.page_source)
        # assert self.browser.page_source.find('install')

    # testing that the correct hash is returned if the user enters 'hello'
    def test_hash_of_hello(self):
        self.browser.get('http://127.0.0.1:8000')
        text = self.browser.find_element_by_id('id_test')  # find html id
        text.send_key('hello')  # simulate the user entering text 'hello'
        self.browser.find_element_by_name('submit').click()
        self.assertIn('2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824', self.browser.page_source)

    def tearDown(self):  # close the browser automatically
        self.browser.quit()


class UnitTestCase(TestCase):

    def test_homepage_template(self):
        response = self.client.get('/')  # give a response for the homepage
        self.assertTemplateUsed(response, 'hashing/home.html')

    # test that we can create a new form and it is valid
    def test_hash_form(self):
        form = HashForm(data={'text': 'hello'})
        self.assertTrue(form.is_valid())
