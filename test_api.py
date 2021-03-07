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
        result = self.app.get('/hello_world')
        self.assertEqual(result.content_type, 'application/json')


    def test_home_data(self):
        """ def data test data "Hello word"
        """
        result = self.app.get('/hello_world')
        # renvoit data
        self.assertEqual(result.data, b'"Hello World"\n')


    def test_home_by_next(self):
        """
        """
        result = self.app.get('/Next/MOSSON')
        self.assertTrue(b'station' in result.data)

    def test_home_by_Next_tram(self):
        """
        """
        result = self.app.get('/prochain/1/COMEDIE/MOSSON')
        self.assertTrue(b'line', 'station', 'direction' in result.data)
    
    def test_home_by_all_lines(self):
        """
        """
        result = self.app.get('/All_lines')
        self.assertTrue(b'' in result.data)


if __name__ == '__main__':
    unittest.main()