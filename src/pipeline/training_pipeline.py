import os
import sys

PROJECT_ROOT = r"D:\pythonProject\Dimond_Price_Prediction"
sys.path.insert(0, os.path.abspath(PROJECT_ROOT))

from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import Dataingestion

import pandas as pd

if __name__=='__main__':
    obj = Dataingestion()
    train_data_path,test_data_path = obj.Initaite_Data_ingestion()