# drops a CSV file, to trigger mlflow training
import pandas as pd
from datetime import date

import os

from airflow.decorators import task

# so can run this Python file as an Airflow task
@task
def perform_etl(filepath):
    df = pd.read_csv(filepath)
    # remove lo-corr features
    cols_to_remove = df.corr().index[abs(df.corr()['quality']) < 0.1].tolist()
    df.drop(cols_to_remove, inplace = True, axis=1)

    # assumes that dir has no . in it!
    filename = filepath.split('.')[0] + '_' + str(date.today()) + '.csv'
    df.to_csv(filename, index = False)
    return filename
