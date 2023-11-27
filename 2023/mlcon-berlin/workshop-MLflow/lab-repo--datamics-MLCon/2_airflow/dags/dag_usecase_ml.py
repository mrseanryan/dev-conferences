from airflow import DAG
#from airflow.operators.python import PythonVirtualenvOperator
from airflow.operators.python import PythonOperator
from datetime import timedelta
import logging

from airflow.decorators import task, dag

import pendulum

import os

import usecase_etl
import usecase_train

log = logging.getLogger(__name__)

default_args = {
    'owner': 'MLCon_berlin',
    'retries': 3,
    'retry_delay': pendulum.duration(minutes = 1)
}

experiment_name = "From DAG"

def x_1(**kwargs):
    print("x_1")
    # ti = kwargs['ti']
    # place = kwargs['place']
    # ti.xcoms_push( key = 'place', value = place)
    return "x_1_returned__Berlin"

def x_2(**kwargs):
    ti = kwargs['ti']

    # place = ti.xcom_pull(key='place', task_ids='virtualenv_classic_1')
    place = ti.xcom_pull(task_ids='task_1')
    # print(f"x_2 - in_1 = {in_1}")
    print(f"x_2 - place: {place}")
    return "x_2_returned"

@dag(
    dag_id="dag_5_py_ML",
    default_args = default_args,
    description="My Py Airflow ML job",
    start_date=pendulum.datetime(2023, 11, 26, tz="UTC"),
    # schedule_interval="@daily",
    # schedule_interval="*/1 * * * *", # every minute
    # schedule_interval = timedelta(seconds=30),
    schedule_interval = None,
    catchup=False,
    tags=["sean"],
)
def dag_function(filepath):
    filename = usecase_etl.perform_etl(filepath)
    # passing fixed experiment name - since when running via airflow, creating experiments via mlflow does not work (!)
    training = usecase_train.do_training(filename, experiment_name)

    # filename >> run

path_root = os.getcwd()
os.chdir("../")
path_data = os.path.join(os.getcwd(), "data", "winequality.csv")

taskflow_dag = dag_function(path_data)
