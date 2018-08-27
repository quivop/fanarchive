from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from fanfic.models import AuthorGroup, Authorship, Fic, FicPart, Pseud
from users.models import User

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

    @classmethod
    def setUpTestData(cls):
        # Add user, pseud, author group, plus needed authorship
        user_1 = User.objects.create(name='user',
                                     email="user@example.com",
                                     password='butts')
        pseud_1 = Pseud.objects.create(pseud_name='pseud',
                                       pseud_owner=user_1)
        group_1 = AuthorGroup.objects.create()
        Authorship.objects.create(author_group=group_1,
                                  author=pseud_1)

        # create a bunch of fics
        number_of_fics = 25
        for fic_num in range(number_of_fics):
            Fic.objects.create(
                fic_title='Fic %s' % fic_num,
                fic_summary='Butts',
                fic_author_group=group_1,
                pub_date=(timezone.now() - timedelta(days=fic_num)))

        # create a bunch of fic parts for one fic
        number_of_fic_parts = 6
        for part_num in range(number_of_fic_parts):
            FicPart.objects.create(
                fic_id=1,
                fic_part_title='Fic Part %s' % part_num,
                pub_date=(timezone.now() - timedelta(days=part_num)))


class IndexViewTest(MyTestCase):

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

    def test_if_404_error_is_handled_correctly(self):
        resp = self.client.get('/yay_404')
        self.assertEqual(resp.status_code, 404)
        self.assertTemplateUsed(resp, '404.html')
