import json

class MakeDataset:
    def __init__(self, data):
        self.data = data
        self.income_groups = self._get_income_groups()
        
        
    def _get_income_groups(self):
        with open('/Users/bharathbeeravelly/Desktop/End-to-End-ML-Project/data/country_income_mapping.json') as f:
            country_income_mapping = json.load(f)
        return country_income_mapping


   
