import unittest
import pandas as pd
import sys


from make_dataset import MakeDataset

class TestMakeDataset(unittest.TestCase):
    def setUp(self):
        # Create a sample dataset
        data = pd.read_csv('/Users/bharathbeeravelly/Desktop/End-to-End-ML-Project/data/raw/Train.csv')
        self.dataset = MakeDataset(data)
        
    def test_make_countries(self):
        transformed_data = self.dataset.make_countries()
        
        # Check if the 'IncomeGroup' column contains any null values
        self.assertFalse(transformed_data['IncomeGroup'].isnull().any())
        
    def test_make_travel(self):
        transformed_data = self.dataset.make_travel()
        
        # Check if the 'travel_with' column contains any null values
        self.assertFalse(transformed_data['travel_with'].isnull().any())
        
    def test_make_people(self):
        transformed_data = self.dataset.make_people()
        
        
        # Check if the 'total_visitors' column contains any null values and print the custom message
        self.assertFalse(transformed_data['total_visitors'].isnull().any())
        
    def test_make_purpose(self):
        transformed_data = self.dataset.make_purpose()
        
        # Check if the 'purpose' column contains any null values
        self.assertFalse(transformed_data['purpose'].isnull().any())
        
    def test_make_activity(self):
        transformed_data = self.dataset.make_activity()
        
        # Check if the 'main_activity' column contains any null values
        self.assertFalse(transformed_data['main_activity'].isnull().any())
        
        # Check if the 'main_activity' column contains only 3 unique values
        self.assertEqual(transformed_data['main_activity'].nunique(), 3)
        
        # Check if the 'main_activity' column contains only the values 'Wildlife', 'Beach' and 'Others'
        self.assertTrue(set(transformed_data['main_activity'].unique()) == {'Wildlife', 'Beach', 'Others'})
        
    def test_make_info(self):
        transformed_data = self.dataset.make_info()
        
        # Check if the 'info_source' column contains any null values
        self.assertFalse(transformed_data['info_source'].isnull().any())
        
        # Check if the 'info_source' column contains only 3 unique values
        self.assertEqual(transformed_data['info_source'].nunique(), 3)
        
        # Check if the 'info_source' column contains only the values 'Agent', 'Friends' and 'Others'
        self.assertTrue(set(transformed_data['info_source'].unique()) == {'Agent', 'Friends', 'Others'})
        
    def test_make_night_mainland(self):
        transformed_data = self.dataset.make_night_mainland()
        
        # Check if the 'night_mainland' column contains any null values
        self.assertFalse(transformed_data['night_mainland'].isnull().any())
        
        # Check if the 'night_mainland' column contains only 3 unique values
        self.assertEqual(transformed_data['night_mainland'].nunique(), 3)
        
        # Check if the 'night_mainland' column contains only the values '0-5', '10-15' and '7+'
        self.assertTrue(set(transformed_data['night_mainland'].unique()) == {'0-5', '10-15', '7+'})
    
    def test_make_night_zanzibar(self):
        transformed_data = self.dataset.make_night_zanzibar()
        
        # Check if the 'night_zanzibar' column contains any null values
        self.assertFalse(transformed_data['night_zanzibar'].isnull().any())
        
        # Check if the 'night_zanzibar' column contains only 2 unique values
        self.assertEqual(transformed_data['night_zanzibar'].nunique(), 2)
        
        # Check if the 'night_zanzibar' column contains only the values '0-5', '10-15' and '7+'
        self.assertTrue(set(transformed_data['night_zanzibar'].unique()) == {0, 1})
        
    def test_make_payment(self):
        transformed_data = self.dataset.make_payment()
        
        # Check if the 'payment_mode' column contains any null values
        self.assertFalse(transformed_data['payment_mode'].isnull().any())
        
        # Check if the 'payment_mode' column contains only 3 unique values
        self.assertEqual(transformed_data['payment_mode'].nunique(), 2)
        
        # Check if the 'payment_mode' column contains only the values 'Cash', 'Credit Card'
        self.assertTrue(set(transformed_data['payment_mode'].unique()) == {'Cash', 'Credit Card'})
    
    def test_make_dataset(self):
        transformed_data = self.dataset.make_dataset()
        self.assertFalse(transformed_data['tour_arrangement'].isnull().any()) #Check if there are any null values in the 'tour_arrangement' column
        
        # Check if the 'package_transport' column contains any null values
        self.assertFalse(transformed_data['package_transport_int'].isnull().any())
        
        # Check if the 'package_accomodation' column contains any null values
        self.assertFalse(transformed_data['package_accomodation'].isnull().any())
        
        # Check if the 'package_food' column contains any null values
        self.assertFalse(transformed_data['package_food'].isnull().any())
        
        # Check if the 'package_transport_tz' column contains any null values
        self.assertFalse(transformed_data['package_transport_tz'].isnull().any())
        
        # Check if the 'package_sightseeing' column contains any null values
        self.assertFalse(transformed_data['package_sightseeing'].isnull().any())
        
        # Check if the 'package_guided_tour' column contains any null values
        self.assertFalse(transformed_data['package_guided_tour'].isnull().any())
        
        # Check if the 'package_insurance' column contains any null values
        self.assertFalse(transformed_data['package_insurance'].isnull().any())
        
        # Check if the 'first_trip_tz' column contains any null values
        self.assertFalse(transformed_data['first_trip_tz'].isnull().any())
        
            
        
        

if __name__ == '__main__':
    unittest.main()