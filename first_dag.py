# bash operator

from datetime import datetime ,  timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args ={
    'owner' : 'Aditya',
    'retries' : 3,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='first_dag',
    default_args=default_args,
    description='trying out first dag',
    start_date=datetime(2024,1,1,10),
    schedule_interval='@daily'
) as dag :
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world , this is airflow task!"
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo will only run after the completion of first task!"
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo this is third task paralel to second task"
    )

    task1 >> [task2 , task3]