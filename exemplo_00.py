import time

def primeira_atividade():
    print('minha primeira atividade')
    time.sleep(2)

def segunda_atividade():
    print('minha segunda atividade')
    time.sleep(2)

def terceira_atividade():
    print('minha terceira atividade')
    time.sleep(2)

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    print('pipeline finalizou')

if __name__ == '__main__':
    pipeline()