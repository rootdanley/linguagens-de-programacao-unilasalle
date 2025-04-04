import os
import time
import datetime
import calendar

def main():
    diretorio = os.getcwd()
    print("Diretório atual:", diretorio)

    agora = datetime.datetime.now()
    print("Data e hora atuais:", agora)

    # Obter o calendário do mês atual
    ano = agora.year
    mes = agora.month
    print("\nCalendário do mês atual:")
    print(calendar.month(ano, mes))

    print("\nPausa de 3 segundos...")
    time.sleep(3)
    print("Fim da pausa.")

if __name__ == "__main__":
    main()
