class Player: 
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

        print(f"Player: {self.name}")

        print(f"  Speed: {self.speed}")

        print(f"  Dribble: {self.dribble}")

        print(f"  Games: {self.games}")

        print(f"  Goals: {self.goals}")

        print(f"  Goals per game average: {self.average:.2f}\n")



# List to store players
team_list = []

# Collect players for the team
team = True

while team:

    answer = input('Please add players to your team (one at a time) (type "end" to finish): ')
    
    if answer.lower() == 'end':

        team = False  # End the loop

        print('Team registration finished.')

    elif answer:

        player = Player(answer)  # Create an instance of the Player class

        team_list.append(player)  # Add the player to the player list

        print(f'Your team so far: {", ".join([p.name for p in team_list])}')


# Collect player skills
for player in team_list:

    speed = int(input(f'Rate {player.name}\'s speed (between 0 and 10): '))

    dribble = int(input(f'Rate {player.name}\'s dribble (between 0 and 10): '))

    player.set_skills(speed, dribble)  # Set player skills

# Collect performance (games and goals) for players
for player in team_list:

    games = int(input(f'How many games has {player.name} played? '))

    goals = int(input(f'How many goals has {player.name} scored? '))

    player.set_performance(games, goals)  # Set games and goals

# Display all player stats
print("\nComplete player statistics:")

for player in team_list:

    player.display_stats()

# #RegistroDeTime #HabilidadesDosJogadores #EstatisticasDosJogadores #PythonClasses #MediaDeGols