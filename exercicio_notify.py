 
import time
from datetime import date, timedelta, datetime
from plyer import notification

data_atual = date.today()

def alerta(nivel, base, etapa):


    if nivel == 1: nivel = "Alerta Baixo"
    if nivel == 2: nivel = "Alerta Médio" 
    if nivel == 3: nivel = "Alerta Alto"  

    notification.notify(
    title='ATENÇÃO: {}'.format(nivel),
    message = 'Falha de carregamento da base {} na etapa {}\n{}'.format(base,etapa,data_atual),
    app_name = '{}'.format("Nome do Aplicativo"),
    timeout = 5 
    )

alerta(nivel= 2, base = "CLIENTES", etapa = "EXTRAÇÃO")