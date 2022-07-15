from tinydb import TinyDB, Query
db = TinyDB('db.json')
players_table = db.table('players')


class Player:

    def __init__(self, first_name, name, birth_date, gender, ranking, tournament, points, opponents):
        self.first_name = first_name
        self.name = name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking
        self.tournament = tournament
        self.points = points
        self.opponents = opponents

    @classmethod
    def serialize_players(cls, players):
        for player in players:
            serialize_player = {'first_name': player.first_name,
                                'name': player.name,
                                'birth_date': player.birth_date,
                                'gender': player.gender,
                                'ranking': player.ranking,
                                'tournament': player.tournament,
                                'points': player.points,
                                'opponents': player.opponents}
            players_table.insert(serialize_player)

    @classmethod
    def unserialize_players(cls):
        table = players_table.all()
        result = []
        for player in table:
            first_name = player['first_name']
            name = player['name']
            birth_date = player['birth_date']
            gender = player['gender']
            ranking = player['ranking']
            tournament = player['tournament']
            points = player['points']
            opponents = player['opponents']
            player_unserialized = Player(first_name=first_name, name=name, birth_date=birth_date, gender=gender,
                                         ranking=ranking, tournament=tournament, points=points, opponents=opponents)
            result.append(player_unserialized)
        return result

    @classmethod
    def clear_players_table(cls):
        players_table.truncate()

    @classmethod
    def update_players_on_db(cls, players):
        Player = Query()
        for player in players:
            players_table.update({'points': player.points}, Player.first_name == player.first_name)
            players_table.update({'opponents': player.opponents}, Player.first_name == player.first_name)

    @classmethod
    def get_all_players_for_a_tournament(cls):
        for player in players_table.all():
            print(player['first_name'] + ' - ' + player['tournament'])
