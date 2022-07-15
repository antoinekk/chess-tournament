from views.playerView import PlayerView
from models.playerModel import Player
from operator import attrgetter


class PlayerController:

    @classmethod
    def create_players(cls, tournament):
        players = PlayerView.ask_for_players_details(8)
        players_list = []
        for player_details in players:
            player = Player(player_details[0],
                            player_details[1],
                            player_details[2],
                            player_details[3],
                            player_details[4],
                            tournament.name,
                            0,
                            [])
            players_list.append(player)
            tournament.players.append(players_list.index(player))
        return players_list

    @classmethod
    def sort_players(cls, players):
        players.sort(key=attrgetter('points'), reverse=True)
        lists = {}
        for player in players:
            lists.setdefault(getattr(player, 'points'), []).append(player)
            for list in lists:
                lists[list].sort(key=attrgetter('ranking'), reverse=True)
        return players

    @classmethod
    def change_ranking(cls, player_score):
        player_score[0].ranking = player_score[1]
        print('the new ranking of the player is: ' + player_score[0].ranking)
