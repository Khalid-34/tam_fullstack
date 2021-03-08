import unittest
from app_fonction import app


class TestApiFlask(unittest.TestCase):

    def setUp(self):
        """ def setup run app
        """
        self.app = app.test_client()
        self.app.testing = True

    

    def test_home_word(self):
        """ Test if the word is includes
        """
        result = self.app.get('/hello_world')
        self.assertTrue(result.data, 'Hello')

    def test_home_type(self):
        """ test_home_type test if te app is j.son content
        """
        result = self.app.get('/All_lines')
        self.assertEqual(result.content_type, 'application/json')


    def test_home_by_next(self):
        """
        """
        result = self.app.get('/Nextt/COMEDIE')
        self.assertTrue(b'ARRET' in result.data)


    def test_home_by_Next_tram(self):
        """
        """
        result = self.app.get('/prochain/1/ANTIGONE/MOSSON')
        self.assertTrue(b'LIGNE' in result.data)
        self.assertTrue(b'ARRET' in result.data)
        self.assertTrue(b'DESTINATION' in result.data)

    def test_home_by_all_lines(self):
        """
        """
        result = self.app.get('/All_lines')
        self.assertTrue(b'' in result.data)


if __name__ == '__main__':
    unittest.main()
