from django.test import TestCase
from django.urls import reverse

from fanarchive.models import Work, WorkPart
from datetime import date, timedelta


class IndexViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create a bunch of works and work parts
        number_of_works = 25
        for work_num in range(number_of_works):
            Work.objects.create(work_title='Work %s' % work_num, work_summary='Butts', date_created = (date.today() - timedelta(days=work_num)))


    def test_if_site_homepage_redirects_to_fanarchive(self):
        '''Going to 'archive.homepage/' should redirect you to the '/fanarchive/' app directory.
        '''
        resp = self.client.get('/')
        self.assertRedirects(resp, expected_url="/fanarchive/", status_code=302, target_status_code=200, fetch_redirect_response=True)

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
        # create a work
        Work.objects.create(work_title="Butts", work_summary="more butts")
        # create a work part
        WorkPart.objects.create(work_part_title="butt beginnings", work_part_text="and so there was, in the beginning, a butt", work_id=1)


    def test_detail_view_url_exists_at_desired_location(self):
        pass

    def test_if_detail_view_uses_correct_template(self):
        pass

    def test_detail_view_displays_work_and_work_part(self):
        pass