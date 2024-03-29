import os 
from carPricePrediction.logging import logger
from carPricePrediction.config.configuration import DataCleaningConfig
import datetime
import pandas as pd

class DataCleaning:
    def __init__(self, config: DataCleaningConfig):
        self.config = config

    def clean_data(self):
        ### Read raw data
        file = os.listdir(self.config.raw_dataset_dir)
        raw_data = os.path.join(self.config.raw_dataset_dir, file[0])
        df = pd.read_csv(raw_data)

        ### Clean Data
        # Drop ID, Model and Levy
        df.drop(['ID','Model','Levy'], axis=1, inplace=True)
        
        # Make Engine volume numerical and create extra feature turbo.
        numerical_values = []
        turbo_indicator = []
        engine_volume = df['Engine volume']
        for value in engine_volume:
            if 'Turbo' in value:
                numerical_values.append(float(value.split()[0]))
                turbo_indicator.append('Yes')
            else:
                numerical_values.append(float(value))
                turbo_indicator.append('No')

        temp_df = pd.DataFrame({'EngineVolume': numerical_values, 'Turbo': turbo_indicator})
        df = pd.concat([df, temp_df], axis=1)
        df.drop(['Engine volume'], axis=1, inplace=True)

        # Make Mileage numerical
        df['Mileage_km'] = [int(value.split()[0]) for value in df['Mileage']]
        df.drop(['Mileage'], axis=1, inplace=True)

        # Change Prod. year to years (from current date)
        current_year = datetime.datetime.now().year
        df['years'] = current_year - df['Prod. year']
        df.drop(['Prod. year'], axis=1, inplace=True)

        # Remove Outliers
        num_features = ['Price', 'EngineVolume', 'Mileage_km']
        for feature in num_features:
            remove_lines = self.get_outliers_index(df,feature)
            df.drop(remove_lines,inplace=True)

        # Drop duplicates
        df.drop_duplicates(inplace=True)

        # Save the cleaned dataset
        file_path = os.path.join(self.config.dataset_dir, 'interim.csv')
        df.to_csv(file_path, index=False)

        logger.info("Clean data saved successfully.")



    # Remove significant extreme outliers from the dataset
    # We will set multiplier=3 to capture them (we can adjust the multiplier)
    def get_outliers_index(self, data, feature):
        """
        Returns the index of significant extreme outliers.
        """
        # Calculate the IQR
        Q1 = data[feature].quantile(0.25)
        Q3 = data[feature].quantile(0.75)
        IQR = Q3 - Q1

        # Define the upper and lower bounds 
        #(4.5 in order to detect outliers significantly far from the median )
        lower_bound = Q1 - 4.5 * IQR
        upper_bound = Q3 + 4.5 * IQR

        # Identify extreme outliers
        extreme_outliers = data[(data[feature] < lower_bound) | (data[feature] > upper_bound)]

        return extreme_outliers[[feature]].index
    