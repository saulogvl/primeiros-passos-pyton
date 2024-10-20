team = True # team é uma variavel que foi utilizada para declarar como 'vedadeiro' 'a palavra "break" funciona de maneira igual'

team_list = []
 
while team: # usado para fazer loops 

   answer = input ('please say players for your team (one at a time)(say "end" for finish): ') # Define 'team' como False para encerrar o loop

   if answer == ('end'):
    
    team = False # Define 'team' como False para encerrar o loop

    print ('team registration finished')

    print (f'your team is: {", ".join(team_list)}') # Mostra a equipe montada

   elif answer: 
     
     team_list.append(answer) # Adiciona o nome do jogador à lista 'team_list'
     
     print(f'your team in moment is {", ".join(team_list)}')  # Mostra a equipe atualizada



habilit = {}

hability = True # Variável para manter o loop de habilidades ativo

while  hability:
  
    players = input(f'please write one name of player for sort(if you want finish your session write "end"): ')
  
    if players == 'end': # Verifica se o usuário deseja encerrar a inserção de habilidades

       hability = False # Encerra o loop de habilidades

    elif players in team_list: # Verifica se o jogador está na lista do time
   
       speed = input('rate the speed between 0 and 10: ') # Coleta a velocidade

       dribble = input('rate the dribble between 0 and 10: ') # Coleta o drible

       habilit[players] = {'speed': speed, 'dribble': dribble}  # Armazena as estatísticas no dicionário

       print(f'updated statues for {players}: speed {speed} and dribble {dribble}') 

    else:

       print('the player is not on the list') # Mensagem de erro caso o jogador não esteja na lista

# Exibe as estatísticas dos jogadores após o loop
print('\nEstastics of players:')

for answer, stats in habilit.items():
  
  print(f'{answer.title()}: Speed {stats["speed"]}, Dribble {stats["dribble"]}')


about_team = {}

average = [] 

true = True # Variável para manter o loop de jogos ativo

all_goals = 0 # Variável para somar todos os gols de um jogador

# Loop para registrar jogos e calcular médias de gols
for player in team_list:

 matches = int(input(f'{player}, how many games he played? '))

 Goals = int(input(f'how many goals did he score in the game {matches}: '))# Coleta o número de gols
        
        # Calcula a média de gols por jogo
 average = Goals / matches

 print(f'the player {player} maked {Goals} in {matches} matches, he has average of {average} goals per game')
 
about_team[player] = {
   
    'speed': speed,

    'dribble': dribble,

    'games': 0,

     'goals': 0,

    'average': 0.0
}

about_team[player]['games'] = matches

about_team[player]['goals'] = Goals

about_team[player]['average'] = average

print("\nEstatísticas dos jogadores:")

for player, stats in about_team.items():
    
    print(f"Player: {player}")

    print(f"  Speed: {stats['speed']}")

    print(f"  Dribble: {stats['dribble']}")

    print(f"  Matches: {stats['games']}")

    print(f"  Goals: {stats['goals']}")

    print(f"  Average of goals : {stats['average']:.2f}\n")
