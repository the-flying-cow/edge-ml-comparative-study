import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from build_logger import get_logger
from generate_data import build_data
from preprocessing import preprocess
from models import train_models

np.random.seed(7)

logger= get_logger(__name__)

def main():


    logger.info('Generate dataset')
    X, y= build_data()

    data= pd.DataFrame(X, columns= ['Feature1', 'Feature2', 'Feature3', 'Feature4', 'Feature5'])
    target= pd.Series(y, name= 'Label')

    scaled_data= preprocess(data)
    X_train, X_test, y_train, y_test= train_test_split(scaled_data, target, test_size= 0.2, stratify= target, random_state= 7)

    train_models(X_train, X_test, y_train, y_test)
    
    logger.info('Training completed')

if __name__ == '__main__':
    logger.info('Start Application')
    main()