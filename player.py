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