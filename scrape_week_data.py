import requests
import bs4


class TeamTotals:
    def __init__(self, points, against, name, win, tie, played):
        self.points = int(points)
        self.points_against = int(against)
        self.name = name
        self.win = int(win)
        self.tie = int(tie)
        self.played = played


class WeekTotals:
    def __init__(self, team_data, player):

        self.player = player
        self.team_data = team_data
        self.total_points = 0
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.total_points_against = 0
        self.differential = 0
        self.find_totals()
        self.record = "" + str(self.wins) + "-" + str(self.losses) + "-" + str(self.ties)
        self.money_won = 0

    def find_totals(self):

        for team in self.team_data:
            self.total_points += team.points
            self.total_points_against += team.points_against
            if team.win == 0 and team.tie == 0 and team.played:
                self.losses += 1
            elif team.win == 1:
                self.wins += 1
            elif team.tie == 1:
                self.ties += 1
        self.differential += self.total_points - self.total_points_against

        self.player.total_points += self.total_points
        self.player.total_points_against += self.total_points_against
        self.player.wins += self.wins
        self.player.losses += self.losses
        self.player.ties += self.ties


class WeekData:
    def __init__(self, players, week_number):
        self.players = players
        self.week_number = week_number
        self.all_teams_data = []
        self.scrape_week_data(self.week_number)
        self.week_var = 'week' + str(week_number) + '_team_data_list'
        self.data_var = 'week' + str(week_number) + 'data'
        self.calculate_players_totals()
        if self.calculate_winnings('offense'):
            getattr(self.calculate_winnings('offense'), self.data_var).money_won += 20
        if self.calculate_winnings('defense'):
            getattr(self.calculate_winnings('defense'), self.data_var).money_won += 20
        if self.calculate_winnings('wins'):
            getattr(self.calculate_winnings('wins'), self.data_var).money_won += 20
        self.calculate_money_won()

    def scrape_week_data(self, week):
        url = 'http://www.nfl.com/scores/2018/REG' + str(week)
        response = requests.get(url)
        html_soup = bs4.BeautifulSoup(response.text, 'html.parser')

        game_containers = html_soup.find_all('div', class_='new-score-box')
        for game in game_containers:

            team1_name = game.div.div.div.find('p', class_='team-name').text

            team1_points = game.div.div.find('p', class_='total-score').text
            if team1_points == '--':
                team1_points = 0

            team1_points_against = game.find('div', class_='home-team').find('p', class_='total-score').text
            if team1_points_against == '--':
                team1_points_against = 0

            team1_win = 0
            team2_win = 0
            team1_tie = 0
            team2_tie = 0
            team1_played = True
            team2_played = True

            if team1_points > team1_points_against:
                team1_win = 1
            elif team1_points < team1_points_against:
                team2_win = 1
            elif team1_points == 0 and team1_points_against == 0:
                team1_played = False
                team2_played = False
            elif team1_points == team1_points_against:
                team1_tie = 1
                team2_tie = 1

            team2_name = game.find('div', class_='home-team').div.find('p', class_='team-name').text
            team2_points = team1_points_against
            team2_points_against = team1_points

            team1 = TeamTotals(team1_points, team1_points_against, team1_name, team1_win, team1_tie, team1_played)
            team2 = TeamTotals(team2_points, team2_points_against, team2_name, team2_win, team2_tie, team2_played)

            self.all_teams_data.append(team1)
            self.all_teams_data.append(team2)

    def calculate_players_totals(self):
        for team in self.all_teams_data:
            if team.name in self.players[0].teams:
                getattr(self.players[0], self.week_var).append(team)
            elif team.name in self.players[1].teams:
                getattr(self.players[1], self.week_var).append(team)
            elif team.name in self.players[2].teams:
                getattr(self.players[2], self.week_var).append(team)
            elif team.name in self.players[3].teams:
                getattr(self.players[3], self.week_var).append(team)
            elif team.name in self.players[4].teams:
                getattr(self.players[4], self.week_var).append(team)
            elif team.name in self.players[5].teams:
                getattr(self.players[5], self.week_var).append(team)
            elif team.name in self.players[6].teams:
                getattr(self.players[6], self.week_var).append(team)

        setattr(self.players[0], self.data_var, WeekTotals(getattr(self.players[0], self.week_var), self.players[0]))
        setattr(self.players[1], self.data_var, WeekTotals(getattr(self.players[1], self.week_var), self.players[1]))
        setattr(self.players[2], self.data_var, WeekTotals(getattr(self.players[2], self.week_var), self.players[2]))
        setattr(self.players[3], self.data_var, WeekTotals(getattr(self.players[3], self.week_var), self.players[3]))
        setattr(self.players[4], self.data_var, WeekTotals(getattr(self.players[4], self.week_var), self.players[4]))
        setattr(self.players[5], self.data_var, WeekTotals(getattr(self.players[5], self.week_var), self.players[5]))
        setattr(self.players[6], self.data_var, WeekTotals(getattr(self.players[6], self.week_var), self.players[6]))

    def calculate_winnings(self, category):

        def find_most_points():
            most_points = self.players[0]
            for player in self.players:
                if getattr(player, self.data_var).total_points > getattr(most_points, self.data_var).total_points:
                    most_points = player
            if getattr(most_points, self.data_var).total_points != 0:
                return most_points
            else:
                return None

        def find_least_points_against():
            least_points = self.players[0]
            for player in self.players:
                if getattr(player, self.data_var).total_points_against < \
                        getattr(least_points, self.data_var).total_points_against:
                    least_points = player
            if getattr(least_points, self.data_var).total_points_against != 0:
                return least_points
            else:
                return None

        def find_most_wins():
            most_wins = self.players[0]
            for player in self.players:
                if getattr(player, self.data_var).wins > getattr(most_wins, self.data_var).wins:
                    most_wins = player
                elif getattr(player, self.data_var).wins == getattr(most_wins, self.data_var).wins:
                    if getattr(player, self.data_var).differential > getattr(most_wins, self.data_var).differential:
                        most_wins = player
            if getattr(most_wins, self.data_var).wins != 0:
                return most_wins
            else:
                return None

        if category == 'offense':
            return find_most_points()
        elif category == 'defense':
            return find_least_points_against()
        elif category == 'wins':
            return find_most_wins()

    def calculate_money_won(self):
        for player in self.players:
            player.total_winnings += getattr(player, self.data_var).money_won
            player.cash_down = 250 - player.total_winnings
