import os


class PlayerView:

    @classmethod
    def check_ranking(cls, ranking):
        check = ranking.isnumeric()
        if check is True:
            ranking = int(ranking)
            if ranking > 0:
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def ask_for_players_details(cls, nb_of_players):
        players_input = []
        i = 0
        while i < nb_of_players:
            player_input = []
            print('You can fill in details about player' + ' ' + str(i+1))
            first_name = input('Enter player first name: ')
            name = input('Enter player name: ')
            birth_date = input('Enter player birth date: ')
            gender = input('Enter player gender: ')
            ranking = input('Enter player ranking: ')
            check = cls.check_ranking(ranking)
            player_input.extend([first_name, name, birth_date, gender, ranking])
            if check is True and '' not in player_input:
                os.system('clear')
                players_input.append(player_input)
                i += 1
            elif check is False:
                print('Ranking has to be a positive number, superior to zero. Try again: ')
            elif '' in player_input:
                print('One or some fields are empty. Please try again: ')
        return players_input

    @classmethod
    def show_created_players(cls, players):
        print('8 players have been added to the tournament: ' + '\n')
        for player in players:
            print(player.first_name)

    @classmethod
    def choose_player_and_score(cls, players):
        players_name = [players[i].name for i in range(0, len(players), 1)]
        print(players_name)
        while True:
            player_choice = input('Enter the name of the player of your choice: ')
            player_score = input('Enter the new ranking of the player: ')
            try:
                for player in players:
                    if player_choice == player.name:
                        return player, player_score
            except Exception:
                pass
