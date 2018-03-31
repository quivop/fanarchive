from django.test import TestCase


class IndexRedirectTest(TestCase):
	def test_if_site_homepage_redirects_to_fanarchive(self):
		'''Going to 'archive.homepage/' redirects you to the '/fanarchive/' app directory.
		'''
		response = self.client.get('/')
		self.assertRedirects(response, expected_url="/fanarchive/", status_code=302, target_status_code=200, fetch_redirect_response=True)


class IndexViewTest(TestCase):
	pass

	# will add stuff later


class DetailViewTest(TestCase):
	pass

	# another placeholder
