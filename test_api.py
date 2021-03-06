import unittest
from app import app


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


    def test_home_by_next(self):
        """Test if the word is includes in next
        """
        result = self.app.get('/Next')
        print(result.data)
        self.assertTrue(b'' in result.data)


    def test_home_by_Next_tram(self):
        """Test if the word is includes in next_tram
        """
        result = self.app.get('/prochain/1/ANTIGONE/MOSSON')
        self.assertTrue(b'LIGNE' in result.data)
        self.assertTrue(b'ARRET' in result.data)
        self.assertTrue(b'DESTINATION' in result.data)

    def test_home_by_all_lines(self):
        """Test if the word is includes in all_lines
        """
        result = self.app.get('/All_lines')
        self.assertTrue(b'' in result.data)


if __name__ == '__main__':
    unittest.main()