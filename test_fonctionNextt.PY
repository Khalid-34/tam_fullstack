import unittest
from fonctions import nextt, all_lines


class TestMethods(unittest.TestCase):
    def test_by_nextt(self):
        """test la fonction next_tram
        """
        self.assertIsInstance(nextt('MOSSON'), dict)
        self.assertNotIsInstance(nextt('MOSSON'), list)
        self.assertEqual(
            {
                "Ligne": "MOSSON", 
                "dest": "ROUVIERE LONGUE", 
                "station": "42", 
                "time": "18:15:00"}, nextt('MOSSON'))
        self.assertNotEqual(
            {
                "Ligne": "MOSSON", 
                "dest": "ROUVIERE LONGUE", 
                "station": "1", 
                "time": "18:15:00"}, nextt('MOSSON'))
        self.assertTrue(
            {
                "Ligne": "MOSSON", 
                "dest": "ROUVIERE LONGUE", 
                "station": "42", 
                "time": "18:15:00"}, nextt('MOSSON'))                            
        self.assertEqual(type(
            {
                "Ligne": "MOSSON", 
                "dest": "ROUVIERE LONGUE", 
                "station": "42", 
                "time": "18:15:00"}
                ), type(nextt('MOSSON')))

    def test_all_lines(self):
        self.assertIsInstance(all_lines(), list)
        self.assertNotIsInstance(all_lines(), dict)



if __name__ == '__main__':
    unittest.main()