from sklearn.preprocessing import StandardScaler
import pandas as pd
from build_logger import get_logger
from format_to_cpp import export_arduino_params

logger= get_logger(__name__)

def preprocess(data: pd.DataFrame) -> pd.DataFrame:
    scaler= StandardScaler()

    try:
        logger.info('scaling feature data')
        scaled_data= scaler.fit_transform(data)

        scaled_data= pd.DataFrame(scaled_data, columns= data.columns)
        
        logger.info(f"Mean: {scaler.mean_}\nScale: {scaler.scale_}")
        with open("../exports/scaler_params.txt", "w") as f:
            f.write("mean:\n")
            f.write(",".join(map(str, scaler.mean_))) # type: ignore
            f.write("\n")

            f.write("scale:\n")
            f.write(",".join(map(str, scaler.scale_))) # type: ignore

        export_arduino_params("Scaler_mean", scaler.mean_, "w")
        export_arduino_params("Scaler_scale", scaler.scale_, "a")
        return scaled_data

    except Exception as e:
        logger.exception('failed to scale data')
        raise