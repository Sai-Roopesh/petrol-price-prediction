import os
import sys
import zipfile
from src.exception import CustomException
from src.petrol_price_prediction import logging
from dataclasses import dataclass
from typing import Tuple
import pandas as pd


@dataclass
class DataIngestionConfig:
    data_path: str = os.path.join('artifacts', 'data')
    train_data_path: str = os.path.join(data_path, 'train.csv')
    test_data_path: str = os.path.join(data_path, 'test.csv')
    sample_submission_path: str = os.path.join(
        data_path, 'sample_submission.csv')


class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self) -> Tuple[str, str, str]:
        logging.info('Initiating data ingestion')
        try:
            os.makedirs(self.ingestion_config.data_path, exist_ok=True)

            df_train = pd.read_csv(
                'research/data/petrol-price-forecasting/train_data.csv')
            logging.info('Reading train data from csv')
            df_train.to_csv(self.ingestion_config.train_data_path, index=False)
            logging.info('Train data saved successfully')

            df_test = pd.read_csv(
                'research/data/petrol-price-forecasting/test_data.csv')
            logging.info('Reading test data from csv')
            df_test.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info('Test data saved successfully')

            df_sample_submission = pd.read_csv(
                'research/data/petrol-price-forecasting/sample_submission.csv')
            logging.info('Reading sample submission data from csv')
            df_sample_submission.to_csv(
                self.ingestion_config.sample_submission_path, index=False)
            logging.info('Sample submission data saved successfully')

            logging.info('Data ingestion completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.sample_submission_path
            )

        except Exception as e:
            logging.error('Error while ingesting data')
            raise CustomException(e, sys)


if __name__ == '__main__':
    data_ingestion = DataIngestion()
    data_ingestion.initiate_data_ingestion()
