import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import mysql.connector

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

#from src.components.model_trainer import ModelTrainerConfig
#from src.components.model_trainer import ModelTrainer
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            db = mysql.connector.connect(host = '18.136.157.135',
                            user = 'dm_team3',
                            password = 'DM!$!Team!27@9!20&',
                            database = 'project_telecom')
            query = 'select * from telecom_churn_data'
            df = pd.read_sql(query, db)
            df.rename(columns={'columns1':'state','columns2':'account_length',
                                    'columns3':'area_code','columns4':'phone','columns5':'international_plan',
                                    'columns6':'vmail_plan','columns7':'vmail_message','columns8':'day_mins',
                                    'columns9':'day_calls','columns10':'day_charge','columns11':'eve_mins',
                                    'columns12':'eve_calls','columns13':'eve_charge','columns14':'night_mins',
                                    'columns15':'night_calls','columns16':'night_charge','columns17':'international_mins',
                                    'columns18':'international_calls','columns19':'international_charge','columns20':'custserv_calls',
                                    'columns21':'churn'}, inplace=True)
            #df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)

        
if __name__=="__main__":
    obj=DataIngestion()
    #obj.initiate_data_ingestion()
    
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
 
'''
    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
'''

