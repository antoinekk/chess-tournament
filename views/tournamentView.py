import os
from operator import attrgetter


class TournamentView:

    @classmethod
    def ask_for_tournament_details(cls):
        while True:
            tournament_input = []
            name = input('Enter the name of the tournament: ')
            place = input('Enter the place of the tournament: ')
            start_date = input('Enter the start date of the tournament: ')
            end_date = input('Enter the end date of the tournament: ')
            time = input('Enter the time control of the tournament (bullet/blitz/rapid): ')
            description = input('Enter the description of the tournament: ')
            tournament_input.extend([name, place, start_date, end_date, time, description])
            if '' not in tournament_input:
                os.system('clear')
                return tournament_input
            else:
                print('One or some fields are empty. Please try again: ')

    @classmethod
    def show_created_tournament(cls, tournament):
        for item in tournament:
            print('A tournament has been created: '+item.name+' - '+item.place+'\n'
                  'Now, you can add players to this tournament !')

    @classmethod
    def choose_a_tournament(cls, tournaments):
        tournaments_name = [tournaments[i].name for i in range(0, len(tournaments), 1)]
        print(tournaments_name)
        while True:
            tournament_choice = input('Enter the name of the tournament of your choice: ')
            try:
                for tournament in tournaments:
                    if tournament_choice == tournament.name:
                        return tournament
            except Exception:
                pass

    @classmethod
    def enter_match_result(cls, match):
        while True:
            answer = input('Enter match result ' + '(' + match.player_one.first_name +
                           ' / ' + match.player_two.first_name + ' / draw) :')
            if answer == match.player_one.first_name or answer == match.player_two.first_name or answer == 'draw':
                os.system('clear')
                return answer
            else:
                print("you must enter one of the values that are in parenthese. Try again: ")

    @classmethod
    def show_top_3(cls, players, tournament):
        print(tournament.name + '\n')
        players.sort(key=attrgetter('points'), reverse=True)
        print('1st' + ' : ' + players[0].first_name + ' - ' + str(players[0].points) + ' points' + '\n'
              '2nd' + ' : ' + players[1].first_name + ' - ' + str(players[1].points) + ' points' + '\n'
              '3rd' + ' : ' + players[2].first_name + ' - ' + str(players[2].points) + ' points')
