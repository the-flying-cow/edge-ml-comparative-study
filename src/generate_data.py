from sklearn.datasets import make_classification
import numpy as np
from typing import Tuple

from build_logger import get_logger
logger= get_logger(__name__)

def build_data() -> Tuple[np.ndarray, np.ndarray]:
    try:
        logger.info('building dataset')
        features, target= make_classification(n_samples= 1000,
                                                n_features= 5,
                                                n_informative= 2,
                                                n_classes= 2,
                                                random_state= 7,
                                                weights= [0.2, 0.8])

    except Exception as e:
        logger.exception('failed to build dataset')
        raise
    
    finally:
        return (features, target)