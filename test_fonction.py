import unittest
from back import next_tram


class TestMethods(unittest.TestCase):
    """test le resultat de la fonction next_tram
    """
    def test_by_next_tram(self):
        self.assertIsInstance(next_tram(1, 'COMEDIE', 'MOSSON'), dict)
        self.assertNotIsInstance(next_tram(1, 'COMEDIE', 'MOSSON'), list)
        self.assertEqual(
            {
                'station': 'COMEDIE',
                'Ligne': '1',
                'dest': 'MOSSON',
                'time': '01 min 20 sec'}, next_tram(1, 'COMEDIE', 'MOSSON'))
        self.assertNotEqual(
            {
                'station': 'COMEDIE',
                'Ligne': '2',
                'dest': 'MOSSON',
                'time': '01 min 20 sec'}, next_tram(1, 'COMEDIE', 'MOSSON'))
        self.assertTrue(
            {
                'station': 'COMEDIE',
                'Ligne': '1',
                'dest': 'MOSSON',
                'time': '01 min 20 sec'}, next_tram(1, 'COMEDIE', 'MOSSON'))
        self.assertEqual(type(
            {
                'station': 'COMEDIE',
                'Ligne': '1',
                'dest': 'MOSSON',
                'time': '01 min 20 sec'}
                ), type(next_tram(1, 'COMEDIE', 'MOSSON')))


if __name__ == '__main__':
    unittest.main()