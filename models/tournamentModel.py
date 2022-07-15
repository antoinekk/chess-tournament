from tinydb import TinyDB, Query
db = TinyDB('db.json')
tournaments_table = db.table('tournaments')


class Tournament:

    def __init__(self, name, place, start_date, end_date, players, rounds_list, time_control, description, rounds):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
        self.rounds_list = rounds_list
        self.time_control = time_control
        self.description = description
        self.rounds = rounds

    @classmethod
    def serialize_tournaments(cls, tournaments):
        for tournament in tournaments:
            serialized_tournament = {'name': tournament.name,
                                     'place': tournament.place,
                                     'start_date': tournament.start_date,
                                     'end_date': tournament.end_date,
                                     'players': tournament.players,
                                     'rounds_list': tournament.rounds_list,
                                     'time_control': tournament.time_control,
                                     'description': tournament.description,
                                     'rounds': tournament.rounds}
            tournaments_table.insert(serialized_tournament)

    @classmethod
    def unserialize_tournaments(cls):
        table = tournaments_table.all()
        result = []
        for tournament in table:
            name = tournament['name']
            place = tournament['place']
            start_date = tournament['start_date']
            end_date = tournament['end_date']
            players = tournament['players']
            rounds_list = tournament['rounds_list']
            time_control = tournament['time_control']
            description = tournament['description']
            rounds = tournament['rounds']
            tournament_unserialized = Tournament(name=name, place=place, start_date=start_date,
                                                 end_date=end_date, players=players,
                                                 rounds_list=rounds_list, time_control=time_control,
                                                 description=description, rounds=rounds)
            result.append(tournament_unserialized)
        return result

    @classmethod
    def clear_tournaments_table(cls):
        tournaments_table.truncate()

    @classmethod
    def update_tournament_on_db(cls, tournament):
        Tournament = Query()
        tournaments_table.update({'players': tournament.players}, Tournament.name == tournament.name)
        tournaments_table.update({'rounds_list': tournament.rounds_list}, Tournament.name == tournament.name)
        tournaments_table.update({'rounds': tournament.rounds}, Tournament.name == tournament.name)

    @classmethod
    def get_all_tournaments(cls):
        for tournament in tournaments_table.all():
            print(tournament['name'] + ' - ' + tournament['place'])

    @classmethod
    def get_rounds_and_matches_for_a_tournament(cls):
        for tournament in tournaments_table.all():
            print(tournament['name'] + ' - ' + str(tournament['rounds_list']))
