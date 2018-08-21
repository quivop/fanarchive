from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from bs4 import BeautifulSoup

import logging
from contextlib import contextmanager

from fanarchive.models import Fic, FicPart
from fanarchive.views import DetailView

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

    # from https://stackoverflow.com/questions/36456827/logging-output-running-django-tests-under-pycharm
    @contextmanager
    def streamhandler_to_console(lggr):
        # Use 'up to date' value of sys.stdout for StreamHandler,
        # as set by test runner.
        stream_handler = logging.StreamHandler(sys.stdout)
        lggr.addHandler(stream_handler)
        yield
        lggr.removeHandler(stream_handler)

    def testcase_log_console(lggr):
        def testcase_decorator(func):
            def testcase_log_console(*args, **kwargs):
                with streamhandler_to_console(lggr):
                    return func(*args, **kwargs)
            return testcase_log_console
        return testcase_decorator

    logging.basicConfig(filename='test_views.log', level=logging.DEBUG)
    logger = logging.getLogger('django_test')

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
        # create a fic with multiple parts
        Fic.objects.create(
            fic_title="Back from the future",
            fic_summary="Yes, I know we're in the past")
        FicPart.objects.create(
            fic_part_title="the future but not like too far",
            fic_part_text="just like next week or something",
            fic_id=3,
            fic_part_number=1)
        FicPart.objects.create(
            fic_part_title="the past",
            fic_part_text="it's another country",
            fic_id=3,
            fic_part_number=2
            )
        FicPart.objects.create(
            fic_part_title="the far future",
            fic_part_text="au: still no hoverboards",
            fic_id=3,
            fic_part_number=3
            )

    def test_detail_view_url_exists_at_desired_location(self):
        resp = self.client.get(reverse('fanarchive:detail', args=[1]))
        self.assertEqual(resp.status_code, 200)

    def test_if_detail_view_uses_correct_template(self):
        resp = self.client.get(reverse('fanarchive:detail', args=[1]))
        self.assertTemplateUsed(resp, 'fanarchive/detail.html')

    def test_detail_view_displays_fic_and_fic_part(self):
        resp = self.client.get(reverse('fanarchive:detail', args=[1]))
        logger = logging.getLogger(__name__)
        soup = BeautifulSoup(resp.content, 'html.parser')
        logger.info("detail view display test")
        # doesn't actually prove the user can see these elements
        # but does prove they exist on the page
        self.assertTrue(soup.find_all("div", class_="fic_meta"))
        self.assertTrue(soup.find_all("article", class_="fic_part"))

    def test_detail_view_displays_fic_part_warning(self):
        resp = self.client.get(reverse('fanarchive:detail', args=[2]))
        logger = logging.getLogger(__name__)
        soup = BeautifulSoup(resp.content, 'html.parser')
        logger.info("detail view warning display test")
        self.assertTrue(soup.find_all("div", class_="fic_meta"))
        self.assertTrue(soup.find_all("p", class_="fic_part warning"));

    def test_detail_view_does_not_display_fic_part_warning(self):
        resp = self.client.get(reverse('fanarchive:detail', args=[1]))
        logger = logging.getLogger(__name__)
        soup = BeautifulSoup(resp.content, 'html.parser')
        logger.info("detail view no warning display test")
        self.assertTrue(soup.find_all("div", class_="fic_meta"))
        self.assertFalse(soup.find_all("p", class_="fic_part warning"));

    def test_detail_view_displays_fic_parts_in_order(self):
        resp = self.client.get(reverse('fanarchive:detail', args=[3]))
        logger = logging.getLogger(__name__)
        soup = BeautifulSoup(resp.content, 'html.parser')
        logger.info("detail view order display test")
        for x, part in enumerate(soup.find_all("article", class_="fic_part")):
            # loop index starts at 0, fic part starts at 1
            self.assertTrue("Part " + str(x+1) in str(part))


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
