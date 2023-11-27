# Apache Airflow README

- from Airbnb

- programmatically author, schedule, monitor workflows

- Python based

- more complex workflows

- a workflow is a DAG (Directed Acyclic Graph) [avoids circular dependencies -> deadlocks]

- easier to manage than cron jobs

- schedule format is like cron
  - `0 4 * * *`
  - `@hourly`

- monitor tasks over time
  - find bottlenecks, problems in the pipeline

- code as doc
- configuration-as-code

- plugins
  - AWS
  - databases

## install airflow

## need tweak for your py version
pip install "apache-airflow[celery]==2.7.3" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.3/constraints-3.8.txt"

## simpler way
https://www.vultr.com/docs/how-to-deploy-apache-airflow-on-ubuntu-20-04/

```
cd ~/src/github/others/MLCon/2_airflow
virtualenv airflow-1
source ./airflow-1/bin/activate
```

```
mkdir -p dags logs plugins

export AIRFLOW_HOME=$(pwd)
```

## create db

- create airflow.cfg  airflow.db
  - sqlite (not for prod!)

```
airflow db migrate
```

- create user

```
airflow users create \
--username admin \
--firstname Sean \
--lastname Ryan \
--role Admin \
--email sean.ryan@mendix.com
```

```
# run webserver
airflow webserver –port 8080
```

NEW terminal
```
source ./airflow-1/bin/activate
export AIRFLOW_HOME=$(pwd)

pip install virtualenv # some examples need this
pip install pendulum

airflow scheduler
```

## Example

```
import logging
import sys
import time
#from pprint import pprint

import pendulum

from airflow import DAG
#from airflow.decorators import task
from airflow.operators.python import PythonVirtualenvOperator

log = logging.getLogger(__name__)

def x():
  pass

with DAG(
    dag_id="example_python_operator",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:
    virtual_classic_1 = PythonVirtualenvOperator(
            task_id="virtualenv_classic",
            requirements="colorama==0.4.0",
            python_callable=x,
        )

    virtual_classic_2 = PythonVirtualenvOperator(
            task_id="virtualenv_classic",
            requirements="colorama==0.4.0",
            python_callable=x,
        )

    virtual_classic_1 >> virtual_classic_2
```
