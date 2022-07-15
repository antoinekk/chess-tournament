import sys
import os
from models.tournamentModel import Tournament
from models.playerModel import Player


class ReportView:

    @classmethod
    def ask_for_report(cls):
        while True:
            answer = input('Report:' + '\n'
                           'type 1 to get all tournaments' + '\n'
                           'type 2 to get players and scores of a tournament' + '\n'
                           'type 3 to get matches and rounds of a tournament' + '\n'
                           'type q to quit')
            if answer == '1':
                os.system('clear')
                Tournament.get_all_tournaments()
            elif answer == '2':
                os.system('clear')
                Player.get_all_players_for_a_tournament()
            elif answer == '3':
                os.system('clear')
                Tournament.get_rounds_and_matches_for_a_tournament()
            elif answer == 'q':
                print('Goodbye !')
                sys.exit()
            else:
                print('You have to enter one of these options : 1,2,3 or q. Try again: ')
