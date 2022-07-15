from views.tournamentView import TournamentView
from models.tournamentModel import Tournament
from models.playerModel import Player
from models.matchModel import Match
from models.roundModel import Round
from controllers.playerController import PlayerController
from operator import attrgetter
from datetime import datetime
now = datetime.now()


class TournamentController:

    @classmethod
    def create_tournament(cls):
        tournament_details = TournamentView.ask_for_tournament_details()
        tournament = Tournament(tournament_details[0],
                                tournament_details[1],
                                tournament_details[2],
                                tournament_details[3],
                                [],
                                [],
                                tournament_details[4],
                                tournament_details[5],
                                4)
        return tournament

    @classmethod
    def create_matches_first_round(cls, players):
        players.sort(key=attrgetter('ranking'))
        players_superior, players_inferior = players[4:], players[:4]
        matches = [Match(players_superior[i], players_superior[i].points,
                   players_inferior[i], players_inferior[i].points) for i in range(0, len(players_superior), 1)]
        return matches

    @classmethod
    def create_round(cls, tournament):
        round = Round('Round' + ' ' + str(len(tournament.rounds_list) + 1), [], now.strftime('%d/%m/%Y %H:%M:%S'), '')
        return round

    @classmethod
    def play_matches(cls, matches, round):
        print('Now, you can fill in matches results for the ' + round.name)
        for match in matches:
            result = TournamentView.enter_match_result(match)
            match.update_score(result)
            match.player_one.opponents.append(match.player_two.first_name)
            match.player_two.opponents.append(match.player_one.first_name)

    @classmethod
    def finish_round(cls, matches, round, tournament):
        for match in matches:
            round.matches.append(([match.player_one.first_name, match.score_player_one],
                                  [match.player_two.first_name, match.score_player_two]))
        round.date_end = now.strftime('%d/%m/%Y %H:%M:%S')
        tournament.rounds_list.append(round.matches)
        tournament.rounds -= 1

    @classmethod
    def create_matches_next_rounds(cls, sorted_players):
        matches = [Match(sorted_players[i], sorted_players[i].points,
                   sorted_players[i+1], sorted_players[i+1].points) for i in range(0, len(sorted_players), 2)]
        part_one, part_two = sorted_players[:4], sorted_players[4:]
        matches_one = [Match(part_one[i], part_one[i].points, part_one[i+2], part_one[i+2].points) for i in range(2)]
        matches_two = [Match(part_two[i], part_two[i].points, part_two[i+2], part_two[i+2].points) for i in range(2)]
        for match in matches:
            check = match.check_if_players_faced_each_other()
            if check is False:
                return matches
            else:
                return matches_one + matches_two

    @classmethod
    def run_last_rounds(cls, tournament, players):
        while tournament.rounds > 0:
            sorted_players = PlayerController.sort_players(players)
            matches = cls.create_matches_next_rounds(sorted_players)
            round = cls.create_round(tournament)
            cls.play_matches(matches, round)
            cls.finish_round(matches, round, tournament)
            Tournament.update_tournament_on_db(tournament)
            Player.update_players_on_db(players)
