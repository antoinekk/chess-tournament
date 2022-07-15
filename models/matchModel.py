class Match:

    def __init__(self, player_one, score_player_one, player_two, score_player_two):
        self.player_one = player_one
        self.score_player_one = score_player_one
        self.player_two = player_two
        self.score_player_two = score_player_two

    def update_score(self, result):
        if result == self.player_one.first_name:
            self.score_player_one += 1
            self.player_one.points += 1
        elif result == self.player_two.first_name:
            self.score_player_two += 1
            self.player_two.points += 1
        elif result == 'draw':
            self.score_player_one += 0.5
            self.score_player_two += 0.5
            self.player_one.points += 0.5
            self.player_two.points += 0.5

    def check_if_players_faced_each_other(self):
        if self.player_one.first_name in self.player_two.opponents:
            return True
        else:
            return False
