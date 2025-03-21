
times_campeonato = (
    'Flamengo', 'Palmeiras', 'São Paulo', 'Atlético-MG', 'Fluminense',
    'Internacional', 'Corinthians', 'Grêmio', 'Santos', 'Fortaleza'
)


print("Os três primeiros colocados:")
for i in range(3):
    print(f"{i+1}º: {times_campeonato[i]}")


print("\nOs últimos três colocados:")
for i in range(7, 10):
    print(f"{i+1}º: {times_campeonato[i]}")


print("\nTimes em ordem alfabética:")
times_alfabeticos = sorted(times_campeonato)
for time in times_alfabeticos:
    print(time)


time_informado = input("\nInforme o nome de um time para saber sua posição: ").strip()

if time_informado in times_campeonato:
    posicao = times_campeonato.index(time_informado) + 1  
    print(f"\nO time {time_informado} está na {posicao}ª posição.")
else:
    print("\nTime não encontrado entre os 10 primeiros colocados.")
