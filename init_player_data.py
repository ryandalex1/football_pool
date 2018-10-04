class Player:
    def __init__(self, teams, name):
        self.teams = teams
        self.name = name
        self.total_points = 0
        self.total_points_against = 0
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.cash_down = 0
        self.total_winnings = 0

        self.week1_team_data_list = []
        self.week1data = None

        self.week2_team_data_list = []
        self.week2data = None

        self.week3_team_data_list = []
        self.week3data = None

        self.week4_team_data_list = []
        self.week4data = None

        self.week5_team_data_list = []
        self.week5data = None

        self.week6_team_data_list = []
        self.week6data = None

        self.week7_team_data_list = []
        self.week7data = None

        self.week8_team_data_list = []
        self.week8data = None

        self.week9_team_data_list = []
        self.week9data = None

        self.week10_team_data_list = []
        self.week10data = None

        self.week11_team_data_list = []
        self.week11data = None

        self.week12_team_data_list = []
        self.week12data = None

        self.week13_team_data_list = []
        self.week13data = None

        self.week14_team_data_list = []
        self.week14data = None

        self.week15_team_data_list = []
        self.week15data = None

        self.week16_team_data_list = []
        self.week16data = None

        self.week17_team_data_list = []
        self.week17data = None


def create_players():

    jt = Player(['Packers', 'Jaguars', 'Raiders', 'Redskins'], "JT")
    paul = Player(['Eagles', 'Giants', 'Ravens', 'Browns'], "Paul")
    alan = Player(['Patriots', '49ers', 'Broncos', 'Colts'], "Alan")
    dan = Player(['Steelers', 'Chiefs', 'Panthers', 'Seahawks'], "Dan")
    marge = Player(['Rams', 'Saints', 'Titans', 'Lions'], "Marge")
    ward = Player(['Falcons', 'Texans', 'Jets', 'Cardinals'], "Ward")
    bruce = Player(['Vikings', 'Chargers', 'Cowboys', 'Bengals'], "Bruce")

    return {'jt': jt, 'paul': paul, 'alan': alan, 'dan': dan, 'marge': marge, 'ward': ward, 'bruce': bruce}
