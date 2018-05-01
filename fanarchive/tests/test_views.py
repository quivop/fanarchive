from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from fanarchive.models import Fic, FicPart


class IndexViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create a bunch of fics and fic parts
        number_of_fics = 25
        for fic_num in range(number_of_fics):
            Fic.objects.create(
                fic_title='Fic %s' % fic_num,
                fic_summary='Butts',
                pub_date=(timezone.now() - timedelta(days=fic_num)))

    def test_if_site_homepage_redirects_to_fanarchive(self):
        '''Going to 'archive.homepage/' should redirect you to the '/fanarchive/' app directory.
        '''
        resp = self.client.get('/')
        self.assertRedirects(
            resp, expected_url="/fanarchive/",
            status_code=302, target_status_code=200,
            fetch_redirect_response=True)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/fanarchive/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('fanarchive:index'))
        self.assertEqual(resp.status_code, 200)

    def test_if_index_view_uses_correct_template(self):
        resp = self.client.get(reverse('fanarchive:index'))
        self.assertEqual(resp.status_code, 200)

        # Leaving this bit commented till I rip out jinja templating

        self.assertTemplateUsed(resp, 'fanarchive/index.html')


class DetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create a fic
        Fic.objects.create(
            fic_title="Butts",
            fic_summary="more butts")
        # create a fic part
        FicPart.objects.create(
            fic_part_title="butt beginnings",
            fic_part_text="and so there was, in the beginning, a butt",
            fic_id=1)

    def test_detail_view_url_exists_at_desired_location(self):
        pass

    def test_if_detail_view_uses_correct_template(self):
        pass

    def test_detail_view_displays_fic_and_fic_part(self):
        pass

from django.http import HttpResponseServerError
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory

class ErrorViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create a bunch of fics and fic parts
        number_of_fics = 3
        for fic_num in range(number_of_fics):
            Fic.objects.create(
                fic_title='Fic %s' % fic_num,
                fic_summary='Butts',
                pub_date=(timezone.now() - timedelta(days=fic_num)))

    @classmethod
    def setUp(self):
        # give every test a fake request
        self.factory = RequestFactory()

    def test_if_404_error_is_handled_correctly(self):
        resp = self.client.get('/yay_404')
        self.assertEqual(resp.status_code, 404)
        self.assertTemplateUsed(resp, '404.html')

    def test_if_500_error_is_handled_correctly(self):
        # leaving this a stub test because it needs selenium to function correctly.
        request = self.factory.get('butts')
        request.user = AnonymousUser()

        def my_test_500_view(request):
            # return a 500 Internal Server Error code
            return HttpResponseServerError()

        resp = my_test_500_view(request)
        self.assertEqual(resp.status_code, 500)
        # self.assertTemplateUsed(resp, '500.html')


# make sure to run:
# `python manage.py collectstatic`
# *before* running these tests

from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class MySeleniumTest(LiveServerTestCase):
    fixtures = ['initial_data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_latest_fics_displayed(self):
        # open homepage
        self.selenium.get('%s%s' % (
            self.live_server_url, ''))
        # check that the 'no fics' error is not displayed
        assert "No fics are available <strong>:sadface:</strong>." not in self.selenium.page_source
