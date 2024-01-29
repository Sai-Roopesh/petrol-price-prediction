from src.exception import CustomException
from src.petrol_price_prediction import logging
import sys

try:
    print(1/0)
except Exception as e:
    logging.error(e)
    raise CustomException(e, error_detail=sys)
