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
    dag_id="dag_2",
    default_args = default_args,
    description="My 2nd Airflow job 2",
    start_date=pendulum.datetime(2023, 11, 26, tz="UTC"),
    # schedule_interval="@daily",
    # schedule_interval="*/1 * * * *", # every minute
    schedule_interval = timedelta(seconds=30),
    catchup=False,
    tags=["sean"]
) as dag:

    task_1 = BashOperator(
        task_id = "task_1__bash",
        bash_command="echo part 1 - Hello from Airflow 3!"
    )

    task_2 = BashOperator(
        task_id = "task_2__bash",
        bash_command="echo part 2 - Hello from Airflow 3!"
    )

    # task 1 first
    task_1 >> task_2

    log.warning("bash ran!")
    # pass
