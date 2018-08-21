from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from fanfic.models import Fic, FicPart

from django.test.utils import override_settings


class MyTestCase(TestCase):
    settings_mgr = override_settings(SECURE_SSL_REDIRECT=False,
                                     CSRF_COOKIE_SECURE=False,
                                     SESSION_COOKIE_SECURE=False)

    @classmethod
    def setUpClass(cls):
        cls.settings_mgr.enable()

        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.settings_mgr.disable()

        super().tearDownClass()


class IndexViewTest(MyTestCase):

    @classmethod
    def setUpTestData(cls):
        # create a bunch of fics and fic parts
        number_of_fics = 25
        for fic_num in range(number_of_fics):
            Fic.objects.create(
                fic_title='Fic %s' % fic_num,
                fic_summary='Butts',
                pub_date=(timezone.now() - timedelta(days=fic_num)))

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/archive/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('fanfic:index'))
        self.assertEqual(resp.status_code, 200)

    def test_if_index_view_uses_correct_template(self):
        resp = self.client.get(reverse('fanfic:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'fanfic/index.html')


class DetailViewTest(MyTestCase):

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
        resp = self.client.get(reverse('fanfic:detail', args=[1]))
        self.assertEqual(resp.status_code, 200)

    def test_if_detail_view_uses_correct_template(self):
        resp = self.client.get(reverse('fanfic:detail', args=[1]))
        self.assertTemplateUsed(resp, 'fanfic/detail.html')

    def test_detail_view_displays_fic_and_fic_part(self):
        pass

    def test_detail_view_displays_fic_part_warning(self):
        pass

    def test_detail_view_does_not_show_future_dated_parts(self):
        pass

    def test_detail_view_displays_fic_parts_in_order(self):
        pass


class ErrorViewUnitTest(MyTestCase):

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
