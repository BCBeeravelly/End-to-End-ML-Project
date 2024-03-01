import json
import pandas as pd


class MakeDataset:
    def __init__(self, data):
        self.data = data
        self.data = self._remove_redunant_columns()
        
    
    def _remove_redunant_columns(self):
        '''
        Remove the 'ID' and 'most_impressing' columns
        ''' 
        self.data = self.data.drop(['ID', 'most_impressing'], axis=1)
        return self.data
        
    
    def make_countries(self):
        '''
        Transform the 'country' column to 'IncomeGroup' column and label encode them as 1, 2, 3, 4
        '''        
        self.data['country'] = self.data['country'].str.title()
        
        with open('/Users/bharathbeeravelly/Desktop/End-to-End-ML-Project/data/references/country_income_mapping.json') as f:
            income_groups = json.load(f)
        self.data['IncomeGroup'] = self.data['country'].map(income_groups)
        self.data = self.data.drop('country', axis=1)  # Drop the 'country' column
        return self.data
    
    
    def make_travel(self):
        '''
        Transform the 'travel_with' column, fill the missing values by the mode of the column and label encode them as 1, 2, 3, 4
        '''
        if self.data['travel_with'].isnull().any():
            print('Detected missing values, filling with the mode')
            self.data['travel_with'] = self.data['travel_with'].fillna(self.data['travel_with'].mode()[0])      
        return self.data
    
    def make_people(self):
        '''
        Make a singular column to store the total no of travelers and drop the columns `total_male` and `total_female`
        '''
        self.data['total_visitors'] = self.data[['total_male', 'total_female']].sum(axis=1, skipna=True)
        self.data['total_visitors'].fillna(self.data['total_visitors'].mean(), inplace=True)
        self.data.loc[self.data['total_visitors'] == 0, 'total_visitors'] = round(self.data['total_visitors'].mean())
        self.data = self.data.drop(['total_male', 'total_female'], axis=1)
        
        return self.data
    
    def make_purpose(self):
        '''
        Group the 'purpose' column into 2 categories: 'Holiday' and 'Others'
        '''
        
        self.data['purpose'] = self.data['purpose'].replace('Leisure and Holidays', 'Holiday')
        self.data['purpose'] = self.data['purpose'].astype(str)
        self.data.loc[self.data['purpose'] != 'Holiday', 'purpose'] = 'Others'
        
        self.data['purpose'].fillna(self.data['purpose'].mode()[0], inplace=True)
        
        return self.data
        
        
    def make_activity(self):
        '''
        Make the 'activity' column to 3 categories: 'Wildlife', 'Beach and 'Others'
        '''
        
        self.data['main_activity'] = self.data['main_activity'].replace('Wildlife tourism', 'Wildlife')
        self.data['main_activity'] = self.data['main_activity'].replace('Beach tourism', 'Beach')
        
        self.data.loc[~self.data['main_activity'].isin(['Wildlife', 'Beach']), 'main_activity'] = 'Others'
        
        self.data['main_activity'].fillna(self.data['main_activity'].mode()[0], inplace=True)
        
        return self.data
    
    def make_info(self):
        '''
        Make the 'info_source' column to 3 categories: 'Agent', 'Friends', 'Advertisement
        '''
        
        self.data['info_source'] = self.data['info_source'].replace('Friends, relatives', 'Friends')
        self.data['info_source'] = self.data['info_source'].replace('Travel, agent, tour operator', 'Agent')
        self.data.loc[~self.data['info_source'].isin(['Friends', 'Agent']), 'info_source'] = 'Others'
        
        self.data['info_source'].fillna(self.data['info_source'].mode()[0], inplace=True)
        
        return self.data
    
    def make_night_mainland(self):
        '''
        Make the 'night_mainland' column to 3 categories: '0-5', '`10-15', '7+'
        '''
        self.data['night_mainland'] = pd.cut(self.data['night_mainland'], bins=[0, 5, 10, float('inf')], labels=['0-5', '10-15', '7+'], right=False)
        self.data['night_mainland'].fillna(self.data['night_mainland'].mode()[0], inplace=True)
        
        
        return self.data
    
    def make_night_zanzibar(self):
        '''
        Make the 'night_zanzibar' column to 2 categories: 0 and 1
        '''
        self.data['night_zanzibar'] = self.data['night_zanzibar'].apply(lambda x: 0 if x == 0 else 1)
        self.data['night_zanzibar'].fillna(self.data['night_zanzibar'].mode()[0], inplace=True)
        
        return self.data
    
    def make_payment(self):
        ''' 
        Make the 'payment' column to 2 categories: 'Cash' and 'Credit Card'
        '''
        self.data['payment_mode'] = self.data['payment_mode'].apply(lambda x: x if x in ['Cash', 'Credit Card'] else None)
        self.data['payment_mode'].fillna(self.data['payment_mode'].mode()[0], inplace=True)
        
        return self.data

        
    def make_dataset(self):
        '''
        Make the entire dataset
        '''
        # self.data = self._remove_redunant_columns()
        self.data = self.make_countries()
        self.data = self.make_travel()
        self.data = self.make_people()
        self.data = self.make_purpose()
        self.data = self.make_activity()
        self.data = self.make_info()
        self.data = self.make_night_mainland()
        self.data = self.make_night_zanzibar()
        
        return self.data
        
        


if __name__ == "__main__":
        # Create an instance of MakeDataset
        data = pd.read_csv('/Users/bharathbeeravelly/Desktop/End-to-End-ML-Project/data/raw/Train.csv')
        dataset = MakeDataset(data)
            
        # # Transform the countries in the dataset
        # transformed_data = dataset.make_countries()
        # transformed_data = dataset.make_travel()
        # transformed_data = dataset.make_people()
        # transformed_data = dataset.make_purpose()
        # transformed_data = dataset.make_activity()
        # transformed_data = dataset.make_info()
        
        transformed_data = dataset.make_dataset()
        
        transformed_data.to_csv('/Users/bharathbeeravelly/Desktop/End-to-End-ML-Project/data/processed/TransformedData.csv')
        
        print(transformed_data.head())
        
   
