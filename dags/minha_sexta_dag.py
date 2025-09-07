import time
from datetime import datetime

from airflow.decorators import dag, task
from airflow.models.baseoperator import chain

@dag(
    dag_id='minha_sexta_dag',
    description='minha etl braba',
    schedule='* * * * *',
    start_date=datetime(2025, 1, 1),
    catchup=False # se for True, o airflow vai executar todas as tarefas que foram perdidas
)

def pipeline():
    @task
    def primeira_atividade():
        return 'ElyFlow não precisa de XCOM'

    @task
    def segunda_atividade(response):
        print(f'minha segunda atividade: {response}')
        time.sleep(2)

    @task
    def terceira_atividade():
        print('minha terceira atividade')
        time.sleep(2)

    @task
    def quarta_atividade():
        print('pipeline finalizou')

    t1 = primeira_atividade()
    t2 = segunda_atividade(t1)
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    chain(t1,t2,t3,t4)

pipeline()
    