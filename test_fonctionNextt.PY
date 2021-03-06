import unittest
from fonctions import next, all_lines


class TestMethods(unittest.TestCase):
    """test by next if the result is equal to the example below
    """
    def test_by_next(self):

        self.assertIsInstance(next(), list)
        self.assertNotIsInstance(next(), dict)
        # self.assertEqual([
        #     {
        #         "ARRET": "MOSSON", 
        #         "DESTINATION": "COURNONSEC", 
        #         "HORAIRE": "12:40:00", 
        #         "LIGNE": "34"
        #     },
        #     {
        #         "ARRET": "MOSSON", 
        #         "DESTINATION": "SAINT-GEORGES", 
        #         "HORAIRE": "13:00:00", 
        #         "LIGNE": "40"
        #     },
        #     {
        #         "ARRET": "MOSSON", 
        #         "DESTINATION": "SAINT-GEORGES", 
        #         "HORAIRE": "14:00:00", 
        #         "LIGNE": "40"
        #         }
        #             ], next('MOSSON'))


        # self.assertNotEqual([
        #     {
        #         "ARRET": "MOSSON", 
        #         "DESTINATION": "COURNONSEC", 
        #         "HORAIRE": "12:40:00", 
        #         "LIGNE": "40"
        #     },
        #     {
        #         "ARRET": "MOSSON", 
        #         "DESTINATION": "SAINT-GEORGES", 
        #         "HORAIRE": "13:00:00", 
        #         "LIGNE": "40"
        #     },
        #     {
        #         "ARRET": "MOSSON", 
        #         "DESTINATION": "SAINT-GEORGES", 
        #         "HORAIRE": "14:00:00", 
        #         "LIGNE": "40"
        #         }
        #             ], next('MOSSON'))

        # self.assertTrue([
        #     {
        #         "ARRET": "MOSSON", 
        #         "DESTINATION": "COURNONSEC", 
        #         "HORAIRE": "12:40:00", 
        #         "LIGNE": "34"
        #     },
        #     {
        #         "ARRET": "MOSSON", 
        #         "DESTINATION": "SAINT-GEORGES", 
        #         "HORAIRE": "13:00:00", 
        #         "LIGNE": "40"
        #     },
        #     {
        #         "ARRET": "MOSSON", 
        #         "DESTINATION": "SAINT-GEORGES", 
        #         "HORAIRE": "14:00:00", 
        #         "LIGNE": "40"
        #         }
        #             ], next('MOSSON'))

        # self.assertEqual(type(
        #     [
        #         {
        #             "ARRET": "MOSSON", 
        #             "DESTINATION": "COURNONSEC", 
        #             "HORAIRE": "12:40:00", 
        #             "LIGNE": "34"
        #         },
        #         {
        #              "ARRET": "MOSSON", 
        #              "DESTINATION": "SAINT-GEORGES", 
        #              "HORAIRE": "13:00:00", 
        #              "LIGNE": "40"
        #         },
        #         {
        #             "ARRET": "MOSSON", 
        #             "DESTINATION": "SAINT-GEORGES", 
        #             "HORAIRE": "14:00:00", 
        #             "LIGNE": "40"
        #         }
        #         ]), type(next('MOSSON')))

    def test_all_lines(self):
        
        """test by all_lines if the result is equal to the example below
        """
        self.assertIsInstance(all_lines(), list)
        self.assertNotIsInstance(all_lines(), dict)



if __name__ == '__main__':
    unittest.main()
