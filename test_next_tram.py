import unittest
from fonctions import next_tram, next


class TestMethods(unittest.TestCase):
    """test by next_tram if the result is equal to the example below
    """
    def test_by_next_tram(self):
        self.assertIsInstance(next_tram(1, 'COMEDIE', 'MOSSON'), dict)
        self.assertNotIsInstance(next_tram(1, 'COMEDIE', 'MOSSON'), list)
        self.assertEqual(
            {  
                "ARRET": "COMEDIE", 
                "ATTENTE": "01 min 51 sec", 
                "DESTINATION": "MOSSON", 
                "LIGNE": "1"}, next_tram(1, 'COMEDIE', 'MOSSON'))
        self.assertNotEqual(
            {  
                "ARRET": "COMEDIE", 
                "ATTENTE": "01 min 51 sec", 
                "DESTINATION": "MOSSON", 
                "LIGNE": "2"}, next_tram(1, 'COMEDIE', 'MOSSON'))
        self.assertTrue(            
            {  
                "ARRET": "COMEDIE", 
                "ATTENTE": "01 min 51 sec", 
                "DESTINATION": "MOSSON", 
                "LIGNE": "1"}, next_tram(1, 'COMEDIE', 'MOSSON'))
        self.assertEqual(type(
            {
                "ARRET": "COMEDIE", 
                "ATTENTE": "01 min 51 sec", 
                "DESTINATION": "MOSSON", 
                "LIGNE": "1"}
                ), type(next_tram(1, 'COMEDIE', 'MOSSON')))



if __name__ == '__main__':
    unittest.main()

