from datetime import timedelta
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from fanarchive.models import Fic, FicPart

from selenium import webdriver
from django.test import LiveServerTestCase


class UnitTestClient(Client):
    def get(self, *args, **kwargs):
        """Request a response from the server using GET."""
        response = super().get(secure=True, *args, **kwargs)
        return response


class IndexViewTest(TestCase):
    client_class = UnitTestClient

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
        pass
        # resp = self.client.get('')
        # self.assertRedirects(
        #     resp, expected_url="/fanarchive/")

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/fanarchive/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('fanarchive:index'))
        self.assertEqual(resp.status_code, 200)

    def test_if_index_view_uses_correct_template(self):
        resp = self.client.get(reverse('fanarchive:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'fanarchive/index.html')


class DetailViewTest(TestCase):
    client_class = UnitTestClient

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
        # create a fic with no parts
        Fic.objects.create(
            fic_title="Big bara tiddies",
            fic_summary="better than butts")
        # create a fic with future parts
        Fic.objects.create(
            fic_title="Back from the future",
            fic_summary="Yes, I know we're in the past")
        FicPart.objects.create(
            fic_part_title="the future but not like too far",
            fic_part_text="just like next week or something",
            fic_id=3)

    def test_detail_view_url_exists_at_desired_location(self):
        resp = self.client.get(reverse('fanarchive:detail', args=[1]))
        self.assertEqual(resp.status_code, 200)

    def test_if_detail_view_uses_correct_template(self):
        resp = self.client.get(reverse('fanarchive:detail', args=[1]))
        self.assertTemplateUsed(resp, 'fanarchive/detail.html')

    def test_detail_view_displays_fic_and_fic_part(self):
        pass

    def test_detail_view_displays_fic_part_warning(self):
        pass

    def test_detail_view_does_not_show_future_dated_parts(self):
        pass

    def test_detail_view_displays_fic_parts_in_order(self):
        pass


class ErrorViewUnitTest(TestCase):
    client_class = UnitTestClient

    @classmethod
    def setUpTestData(cls):
        # create a bunch of fics and fic parts
        number_of_fics = 3
        for fic_num in range(number_of_fics):
            Fic.objects.create(
                fic_title='Fic %s' % fic_num,
                fic_summary='Butts',
                pub_date=(timezone.now() - timedelta(days=fic_num)))

    def test_if_404_error_is_handled_correctly(self):
        resp = self.client.get('/yay_404')
        self.assertEqual(resp.status_code, 404)
        self.assertTemplateUsed(resp, '404.html')


class SeleniumTest(LiveServerTestCase):

    @classmethod
    def setUp(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(10)
        cls.browser.profile = webdriver.FirefoxProfile()
        cls.browser.profile.accept_untrusted_certs = True
        super().setUpClass()

    @classmethod
    def tearDown(cls):
        cls.browser.quit()

    def test_if_site_is_served_securely(self):
        self.browser.get(self.live_server_url)

        self.assertIn("https://127.0.0.1:8000", self.browser.current_url)
        self.fail('your fics are not secure!!')
