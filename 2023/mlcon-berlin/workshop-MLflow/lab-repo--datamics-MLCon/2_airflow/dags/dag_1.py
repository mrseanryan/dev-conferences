from airflow import DAG
#from airflow.operators.python import PythonVirtualenvOperator
from airflow.operators.bash import BashOperator
from datetime import timedelta
import logging

import pendulum

log = logging.getLogger(__name__)

default_args = {
    'owner': 'MLCon_berlin',
    'retries': 3,
    'retry_delay': pendulum.duration(seconds = 2)
}

with DAG(
    dag_id="dag_1",
    default_args = default_args,
    description="My first Airflow job",
    start_date=pendulum.datetime(2023, 11, 26, tz="UTC"),
    # schedule_interval="@daily",
    # schedule_interval="*/1 * * * *", # every minute
    # schedule_interval = timedelta(seconds=30),
    schedule_interval = None,
    catchup=False,
    tags=["sean"]
) as dag:

    task_1 = BashOperator(
        task_id = "task_1__bash",
        bash_command="echo Hello from Airflow 3!"
    )

    log.warning("bash ran!")
    # pass
