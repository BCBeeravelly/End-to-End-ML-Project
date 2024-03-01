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
    
    def test_make_package(self):
        
        # Check if the 'package' column contains any null values
        self.assertFalse(self.dataset.tour_arrangement.isnull().any())
        
        # Check if the 'package' column contains only 2 unique values
        self.assertEqual(self.dataset.tour_arrangement.nunique(), 2)
        
        # Check if the 'package' column contains only the values 'Independent' and 'Package Tour'
        self.assertTrue(set(self.dataset.tour_arrangement.unique()) == {'Independent', 'Package Tour'})
        
    
        
       
        
        
        
        

if __name__ == '__main__':
    unittest.main()