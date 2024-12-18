# Definição da classe Player para armazenar estatísticas de jogadores

class Player:
    
    def __init__(self, name):
        
        # Inicializa o jogador com nome e estatísticas zeradas
        self.name = name

        self.speed = 0

        self.dribble = 0

        self.games = 0

        self.goals = 0

        self.average_goals = 0.0


    def set_skills(self, speed, dribble):
        
        # Define as habilidades do jogador (velocidade e drible)

        self.speed = speed

        self.dribble = dribble


    def set_stats(self, games, goals):
        
        # Define as estatísticas de jogos e calcula a média de gols por jogo

        self.games = games

        self.goals = goals

        self.average_goals = goals / games if games > 0 else 0.0

    def __str__(self):
        
        # Retorna uma string formatada com as informações do jogador

        return (f"{self.name} -> Speed: {self.speed}, Dribble: {self.dribble}, "
                
                f"Games: {self.games}, Goals: {self.goals}, Average Goals: {self.average_goals:.2f}")
    


# Lista para armazenar os nomes dos jogadores e dicionário para instâncias
team_list = []

players_dict = {}


team = True  # Controle do loop de criação do time


# Adicionando jogadores ao time

while team:
    
    answer = input('Enter a player name for the team (or "end" to finish): ')

    if answer.lower() == 'end':
        
        # Termina o loop quando 'end' é digitado

        team = False

        print("\nTeam registration finished.")

        print(f"Your team is: {', '.join(team_list)}")

    elif answer:
        # Adiciona o jogador à lista e cria uma instância de Player

        team_list.append(answer)

        players_dict[answer] = Player(answer)

        print(f"Your current team: {', '.join(team_list)}")

# Adicionando habilidades aos jogadores
hability = True

while hability:
    
    player_name = input('Enter the player’s name to set skills (or "end" to finish): ')

    if player_name.lower() == 'end':
        
        # Termina o loop quando 'end' é digitado

        hability = False

    elif player_name in players_dict:
        
        try:
            
            # Solicita velocidade e drible e os define para o jogador

            speed = int(input('Rate speed between 0 and 10: '))

            dribble = int(input('Rate dribble between 0 and 10: '))

            players_dict[player_name].set_skills(speed, dribble)

            print(f"Updated stats for {player_name}: Speed {speed}, Dribble {dribble}")

        except ValueError:
            
            print("Please enter valid integer ratings for speed and dribble.")

    else:
        
        print("Player not found in the team list.")



# Registrando jogos e gols para calcular médias

for player_name in team_list:
    try:
        
        # Solicita o número de jogos e gols e calcula a média de gols por jogo

        games = int(input(f"{player_name}, number of games played: "))

        goals = int(input(f"{player_name}, total goals scored: "))

        players_dict[player_name].set_stats(games, goals)

        print(f"{player_name} played {games} games, scored {goals} goals, "
              
              f"with an average of {players_dict[player_name].average_goals:.2f} goals per game.")
        
    except ValueError:
        
        print("Please enter valid integers for games and goals.")

# Exibindo as estatísticas finais dos jogadores

print("\nFinal statistics of players:")

for player in players_dict.values():
    
    # Imprime as estatísticas de cada jogador usando o método __str__

    print(player)