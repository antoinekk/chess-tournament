import os
from controllers.tournamentController import TournamentController
from controllers.playerController import PlayerController
from views.reportView import ReportView
from views.playerView import PlayerView
from views.tournamentView import TournamentView
from models.tournamentModel import Tournament
from models.playerModel import Player
from tinydb import TinyDB
db = TinyDB('db.json')
tournaments_table = db.table('tournaments')
players_table = db.table('players')

if __name__ == "__main__":

    menu_options = {
        1: 'Create tournament',
        2: 'Add players',
        3: 'Run tournament',
        4: 'Get report',
        5: 'Change players ranking',
        6: 'Exit',
        }

    def print_menu():
        for key in menu_options.keys():
            print(key, '-', menu_options[key])

    while True:

        print_menu()
        option = ''

        try:
            option = int(input('Enter your choice: '))
            os.system('clear')
        except Exception:
            print('Wrong input. Please enter a number ...')

        if option == 1:

            tournament = [TournamentController.create_tournament()]
            Tournament.serialize_tournaments(tournament)
            TournamentView.show_created_tournament(tournament)

        elif option == 2:

            tournaments_list = Tournament.unserialize_tournaments()
            if len(tournaments_list) == 0:
                os.system('clear')
                print('You must create a tournament first !')
            else:
                tournament = TournamentView.choose_a_tournament(tournaments_list)
                if len(tournament.players) < 8:
                    players = PlayerController.create_players(tournament)
                    Player.serialize_players(players)
                    Tournament.clear_tournaments_table()
                    Tournament.serialize_tournaments(tournaments_list)
                    PlayerView.show_created_players(players)
                else:
                    os.system('clear')
                    print('Players have already been added !')

        elif option == 3:

            tournaments_list = Tournament.unserialize_tournaments()
            if len(tournaments_list) == 0:
                os.system('clear')
                print('You must create a tournament first !')
            else:
                tournament = TournamentView.choose_a_tournament(tournaments_list)
                if tournament.rounds > 0 and len(tournament.players) > 0:
                    all_players = Player.unserialize_players()
                    players = []
                    for player in all_players:
                        if player.tournament == tournament.name:
                            players.append(player)
                    matches_first_round = TournamentController.create_matches_first_round(players)
                    first_round = TournamentController.create_round(tournament)
                    TournamentController.play_matches(matches_first_round, first_round)
                    TournamentController.finish_round(matches_first_round, first_round, tournament)
                    tournaments_table.truncate()
                    players_table.truncate()
                    Tournament.serialize_tournaments(tournaments_list)
                    Player.serialize_players(all_players)
                    TournamentController.run_last_rounds(tournament, players)
                    TournamentView.show_top_3(players, tournament)
                elif tournament.rounds == 0:
                    os.system('clear')
                    print('All the rounds have been played for this tournament')
                elif len(tournament.players) == 0:
                    os.system('clear')
                    print('You must add players before runing the tournament')

        elif option == 4:

            ReportView.ask_for_report()

        elif option == 5:

            players = Player.unserialize_players()
            player_score = PlayerView.choose_player_and_score(players)
            PlayerController.change_ranking(player_score)
            Player.serialize_players(players)

        elif option == 6:

            os.system('clear')
            print('Goodbye !')
            exit()

        else:
            print('Invalid option. Please enter a number between 1 and 6.')
