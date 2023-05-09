import os
import sys

PROJECT_ROOT = r"D:\pythonProject\Dimond_Price_Prediction"
sys.path.insert(0, os.path.abspath(PROJECT_ROOT))

from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import Dataingestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import Model_Trainer

import pandas as pd

if __name__=='__main__':
    obj = Dataingestion()
    train_data_path,test_data_path = obj.Initaite_Data_ingestion()

    data_transformation = DataTransformation()
    train_arr,test_arr,_= data_transformation.Initiate_data_transformation(train_data_path,test_data_path)

    model_trainer = Model_Trainer()
    model_trainer.initiate_model_training(train_arr,test_arr)



