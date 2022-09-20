from django.test import TestCase, Client

import mywatchlist

# Create your tests here.

class watchlist_test(TestCase):
    def test_json(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)


    def test_html(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)


    def test_xml(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)

    # def test_html_template(self):
    #     response = Client().get('/mywatchlist/html/')
    #     self.assertTemplateUsed(response, 'mywatchlist.html')
