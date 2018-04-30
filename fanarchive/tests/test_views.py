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

    def test_if_404_error_is_handled_correctly(self):
        resp = self.client.get('/yay_404')
        self.assertEqual(resp.status_code, 404)
        self.assertTemplateUsed(resp, '404.html')

    def test_if_500_error_is_handled_correctly(self):
        # leaving this a stub test because it needs selenium to function correctly.

        pass
