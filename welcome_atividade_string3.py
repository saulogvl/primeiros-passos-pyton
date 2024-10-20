class Player: #A classe player
    
    def __init__(self, name):

        self.name = name

        self.speed = 0

        self.dribble = 0

        self.games = 0

        self.goals = 0

        self.average = 0.0

    def set_skills(self, speed, dribble):
        #Define as habilidades do jogador.

        self.speed = speed

        self.dribble = dribble

    def set_performance(self, games, goals):
        #Define o desempenho do jogador em termos de jogos e gols.

        self.games = games

        self.goals = goals

        if games > 0:

            self.average = goals / games

        else:

            self.average = 0

    def display_stats(self):

        #Exibe as estatísticas completas do jogador.
        print(f"Jogador: {self.name}")

        print(f"  Velocidade: {self.speed}")

        print(f"  Drible: {self.dribble}")

        print(f"  Jogos: {self.games}")

        print(f"  Gols: {self.goals}")

        print(f"  Média de gols: {self.average:.2f}\n")
    


# Lista para armazenar os jogadores
team_list = []

# Coletar os jogadores para o time

team = True

while team:

    answer = input('Por favor, adicione jogadores ao seu time (um de cada vez) (digite "end" para finalizar): ')
    
    if answer.lower() == 'end':

        team = False  # finaliza o loop

        print('Cadastro de time finalizado.')

    elif answer:

        player = Player(answer)  # Cria uma instância da classe Player

        team_list.append(player)  # Adiciona o jogador à lista de jogadores

        print(f'Seu time no momento é: {", ".join([p.name for p in team_list])}')



# Coletar habilidades dos jogadores
for player in team_list:

    speed = int(input(f'Avalie a velocidade de {player.name} (entre 0 e 10): '))

    dribble = int(input(f'Avalie o drible de {player.name} (entre 0 e 10): '))

    player.set_skills(speed, dribble)  # Define as habilidades do jogador

# Coletar desempenho (jogos e gols) dos jogadores
for player in team_list:

    games = int(input(f'Quantos jogos {player.name} jogou? '))

    goals = int(input(f'Quantos gols {player.name} marcou? '))

    player.set_performance(games, goals)  # Define os jogos e gols

# Exibir todas as estatísticas dos jogadores
print("\nEstatísticas completas dos jogadores:")

for player in team_list:

    player.display_stats()