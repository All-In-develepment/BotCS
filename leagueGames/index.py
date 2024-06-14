import schedule
import time
from update_script import update_database

# Agendar a tarefa para executar uma vez por dia às 2h da manhã
schedule.every().day.at("11:20").do(update_database)

# Função para manter o agendamento em execução
def run_schedule():
    print('Rotina iniciada')
    while True:
        schedule.run_pending()
        time.sleep(60)  # Aguardar um minuto entre as execuções

if __name__ == "__main__":
    run_schedule()
