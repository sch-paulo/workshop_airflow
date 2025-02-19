import time
from loguru import logger

logger.add('execution_logs.log', format='{time} - {message}', level='INFO', rotation='1 day')

def primeira_atividade():
    logger.info('minha primeira atividade')
    time.sleep(2)

def segunda_atividade():
    logger.info('minha segunda atividade')
    time.sleep(2)

def terceira_atividade():
    logger.info('minha terceira atividade')
    time.sleep(2)

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    logger.info('pipeline finalizou')

if __name__ == '__main__':
    while True:
        pipeline()
        time.sleep(10)