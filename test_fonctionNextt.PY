import unittest
from fonctions import nextt, all_lines


class TestMethods(unittest.TestCase):
    def test_by_nextt(self):
        """test la fonction next_tram
        """
        self.assertIsInstance(nextt('MOSSON'), list)
        self.assertNotIsInstance(nextt('MOSSON'), dict)
        self.assertEqual([
            {
                "ARRET": "MOSSON", 
                "DESTINATION": "COURNONSEC", 
                "HORAIRE": "12:40:00", 
                "LIGNE": "34"
            },
            {
                "ARRET": "MOSSON", 
                "DESTINATION": "SAINT-GEORGES", 
                "HORAIRE": "13:00:00", 
                "LIGNE": "40"
            },
            {
                "ARRET": "MOSSON", 
                "DESTINATION": "SAINT-GEORGES", 
                "HORAIRE": "14:00:00", 
                "LIGNE": "40"
                }
                    ], nextt('MOSSON'))


        self.assertNotEqual([
            {
                "ARRET": "MOSSON", 
                "DESTINATION": "COURNONSEC", 
                "HORAIRE": "12:40:00", 
                "LIGNE": "40"
            },
            {
                "ARRET": "MOSSON", 
                "DESTINATION": "SAINT-GEORGES", 
                "HORAIRE": "13:00:00", 
                "LIGNE": "40"
            },
            {
                "ARRET": "MOSSON", 
                "DESTINATION": "SAINT-GEORGES", 
                "HORAIRE": "14:00:00", 
                "LIGNE": "40"
                }
                    ], nextt('MOSSON'))

        self.assertTrue([
            {
                "ARRET": "MOSSON", 
                "DESTINATION": "COURNONSEC", 
                "HORAIRE": "12:40:00", 
                "LIGNE": "34"
            },
            {
                "ARRET": "MOSSON", 
                "DESTINATION": "SAINT-GEORGES", 
                "HORAIRE": "13:00:00", 
                "LIGNE": "40"
            },
            {
                "ARRET": "MOSSON", 
                "DESTINATION": "SAINT-GEORGES", 
                "HORAIRE": "14:00:00", 
                "LIGNE": "40"
                }
                    ], nextt('MOSSON'))

        self.assertEqual(type(
            [
                {
                    "ARRET": "MOSSON", 
                    "DESTINATION": "COURNONSEC", 
                    "HORAIRE": "12:40:00", 
                    "LIGNE": "34"
                },
                {
                     "ARRET": "MOSSON", 
                     "DESTINATION": "SAINT-GEORGES", 
                     "HORAIRE": "13:00:00", 
                     "LIGNE": "40"
                },
                {
                    "ARRET": "MOSSON", 
                    "DESTINATION": "SAINT-GEORGES", 
                    "HORAIRE": "14:00:00", 
                    "LIGNE": "40"
                }
                ]), type(nextt('MOSSON')))

    def test_all_lines(self):
        self.assertIsInstance(all_lines(), list)
        self.assertNotIsInstance(all_lines(), dict)



if __name__ == '__main__':
    unittest.main()
