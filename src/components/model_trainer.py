import os
import sys

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object

import pandas as pd
import numpy as np

from dataclasses import dataclass

#Model Training
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge,Lasso
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import RandomizedSearchCV
from catboost import CatBoostRegressor
from xgboost import XGBRegressor


@dataclass
class ModelTrainerConfig:
    trained_model_train_path = os.path.join('artifacts','model.pkl')


class Model_Trainer:
    def __init__(self):
        self.Model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self,train_arr,test_arr):
        try:
            logging.info('Splitting Dependent and Independent features')
            x_train,y_train,x_test,y_test = (

            )
        except:
            pass


