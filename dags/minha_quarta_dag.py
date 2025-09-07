import time
from datetime import datetime

from airflow.decorators import dag, task

@dag(
    dag_id='minha_quarta_dag',
    description='minha etl braba',
    schedule='* * * * *',
    start_date=datetime(2025, 1, 1),
    catchup=False # se for True, o airflow vai executar todas as tarefas que foram perdidas
)

def pipeline():
    @task
    def primeira_atividade():
        print('minha primeira atividade')
        time.sleep(2)

    @task
    def segunda_atividade():
        print('minha segunda atividade')
        time.sleep(2)

    @task
    def terceira_atividade():
        print('minha terceira atividade')
        time.sleep(2)

    @task
    def quarta_atividade():
        print('pipeline finalizou')

    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    t1 >> [t2, t3]
    t3 << t4

pipeline()
    