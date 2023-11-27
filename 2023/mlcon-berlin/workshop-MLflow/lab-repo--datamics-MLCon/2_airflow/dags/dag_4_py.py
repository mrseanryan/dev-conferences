from airflow import DAG
#from airflow.operators.python import PythonVirtualenvOperator
from airflow.operators.python import PythonOperator
from datetime import timedelta
import logging

import pendulum

log = logging.getLogger(__name__)

default_args = {
    'owner': 'MLCon_berlin',
    'retries': 3,
    'retry_delay': pendulum.duration(seconds = 2)
}

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

with DAG(
    dag_id="dag_4_py",
    default_args = default_args,
    description="My Py Airflow job 2",
    start_date=pendulum.datetime(2023, 11, 26, tz="UTC"),
    # schedule_interval="@daily",
    # schedule_interval="*/1 * * * *", # every minute
    schedule_interval = timedelta(seconds=30),
    catchup=False,
    tags=["sean"],
) as dag:
    task_1 = PythonOperator(
            task_id="task_1",
            python_callable=x_1,
            provide_context=True,
            # dag = DAG,
            # op_kwargs={
            #     'place': 'Berlin'
            # }
        )

    task_2 = PythonOperator(
            task_id="task_2",
            python_callable=x_2,
            provide_context=True,
            # dag = DAG,
        )

    # task 1 first
    task_1 >> task_2

    # parallel
    # [task_1, task_2]

    log.warning("py ran!")
    # pass
