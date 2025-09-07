import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

minha_dag = DAG(
    dag_id='minha_segunda_dag',
    start_date=datetime.datetime(2025, 1, 1),
    schedule='@daily',
    catchup=False
)

EmptyOperator(task_id='tarefa', dag=minha_dag)