from selenium import webdriver
from django.test import LiveServerTestCase, tag
from django.test.utils import override_settings


@tag('selenium')
class SeleniumTest(LiveServerTestCase):
    settings_mgr = override_settings(SECURE_SSL_REDIRECT=False,
                                     CSRF_COOKIE_SECURE=False,
                                     SESSION_COOKIE_SECURE=False)

    @classmethod
    def setUp(cls):
        cls.settings_mgr.enable()

        cls.selenium = webdriver.Firefox()
        cls.selenium.implicitly_wait(15)

        super().setUpClass()

    @classmethod
    def tearDown(cls):
        cls.settings_mgr.disable()

        cls.selenium.quit()

    def test_if_selenium_sees_the_site(self):
        browser = self.selenium
        browser.get(self.live_server_url)

        self.assertEqual('HELL WELCOMES U', browser.title)
