from flask import url_for
from metabrainz import create_app
from metabrainz.testing import FlaskTestCase


class IndexViewsTestCase(FlaskTestCase):

    def test_homepage(self):
        response = self.client.get(url_for('index.home'))
        self.assert200(response)

    def test_contact(self):
        response = self.client.get(url_for('index.contact'))
        self.assert200(response)

    def test_socialcontract(self):
        response = self.client.get(url_for('index.socialcontract'))
        self.assert200(response)

    def test_about(self):
        response = self.client.get(url_for('index.about'))
        self.assert200(response)

    def test_projects(self):
        response = self.client.get(url_for('index.projects'))
        self.assert200(response)

    def test_team(self):
        response = self.client.get(url_for('index.team'))
        self.assert200(response)

    def test_sponsors(self):
        response = self.client.get(url_for('index.sponsors'))
        self.assert200(response)

    def test_bad_customers(self):
        response = self.client.get(url_for('index.bad_customers'))
        self.assert200(response)

    def test_privacy_policy(self):
        response = self.client.get(url_for('index.privacy_policy'))
        self.assert200(response)

    def test_about_customers(self):
        response = self.client.get(url_for('index.about_customers_redirect'))
        self.assertRedirects(response, url_for('users.supporters_list'))

    def test_flask_debugtoolbar(self):
        """ Test if flask debugtoolbar is loaded correctly

        Creating an app with default config so that debug is True
        and SECRET_KEY is defined.
        """
        app = create_app(debug=True)
        client = app.test_client()
        resp = client.get('/about')
        self.assert200(resp)
        self.assertIn('flDebug', str(resp.data))
