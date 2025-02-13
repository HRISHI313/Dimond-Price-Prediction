import os
import sys

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

import pandas as pd
import numpy as np

from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_traformation_config = DataTransformationConfig()

    def get_data_transformation(self):
        logging.info('Initiating Data Transformation')
        try:
            categorical_cols = ['cut','color','clarity']
            numerical_cols = ['carat','depth','table','x','y','z']

            cut_categories = ['Fair','Good','Very Good','Premium','Ideal']
            color_categories = ['D','E','F','G','H','I','J']
            clarity_categories = ['SI2', 'SI1', 'VS1', 'VS2', 'VVS2', 'VVS1', 'I1', 'IF']

            logging.info('Pipeline Initiated')

            num_pipeline = Pipeline(
                steps = [
                    ('imputer',SimpleImputer(strategy = 'median')),
                    ('scaler',StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps = [
                    ('imputer',SimpleImputer(strategy = 'most_frequent')),
                    ('ordinalencoder',OrdinalEncoder(categories = [cut_categories,color_categories,clarity_categories])),
                    ('scaler',StandardScaler())
                ]
            )

            preprocessor = ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_cols),
                ('cat_pipeline',cat_pipeline,categorical_cols)
            ])

            return preprocessor

            logging.info('Data pipeline completed')

        except Exception as e:
            logging.exception('Error occurred in Data ingestion Config: %s', e)


    def Initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Read train and test data completed')
            logging.info(f'Train DataFrame Head : \n{train_df.head().to_string()}')
            logging.info(f'Test DataFrame Head : \n{test_df.head().to_string()}')

            logging.info('Obtaining Preprocessing object')

            preprocessing_obj = self.get_data_transformation()

            target_column_name = 'price'
            drop_column = [target_column_name,'id']

            input_feature_train_df = train_df.drop(columns = drop_column,axis = 1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns = drop_column,axis = 1)
            target_feature_test_df = test_df[target_column_name]

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            logging.info('Applying preprocessing object on training dataframe and testing dataframe')

            train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            save_object(
                file_path=self.data_traformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )
            logging.info('Preprocessor pickle is created and saved')

            return (
                train_arr,
                test_arr,
                self.data_traformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            logging.exception('Error occurred in Data ingestion Config: %s', e)













        except:
            pass



