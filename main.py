from scrape_week_data import *
from init_player_data import *


def main():

    print('Loading Scores\n...')
    player_dict = create_players()
    for week in range(1, 18):
        WeekData(list(player_dict.values()), week)  # this_weeks_data =

    while True:
        week = input('Week? (total, #)\n')
        week_data_var = 'week' + str(week) + 'data'
        player = input('Player? (summary, lowercase name)\n')

        if week == 'total':

            if player == 'summary':

                for new_player in player_dict.keys():
                    print(player_dict[new_player].name)
                    print(str(player_dict[new_player].wins) + "-" + str(player_dict[new_player].losses) +
                          "-" + str(player_dict[new_player].ties))

                    print(str(player_dict[new_player].total_points) + ' - ' +
                          str(player_dict[new_player].total_points_against) + " (" +
                          str(player_dict[new_player].total_points-player_dict[new_player].total_points_against) + ')')

                    print('$' + str(player_dict[new_player].total_winnings) + '\n')
                print('\n\n')

            else:
                print('\n\n' + player_dict[player].name + '\n')
                for team in player_dict[player].teams:
                    print(team)
                print("\n")
                print("Record          ->  " + str(player_dict[player].wins) + "-" + str(player_dict[player].losses) +
                      "-" + str(player_dict[player].ties))
                print("Total Offense   ->  " + str(player_dict[player].total_points))
                print("Total Defense   ->  " + str(player_dict[player].total_points_against))
                print("Differential    ->  " + str(player_dict[player].total_points -
                                                   player_dict[player].total_points_against))
                print("Money Won       ->  $" + str(player_dict[player].total_winnings))
                print("To Break Even   ->  $" + str(player_dict[player].cash_down) + '\n\n')

        else:
            if player == 'summary':
                for player in player_dict.values():
                    print(player.name)
                    print(getattr(player, week_data_var).record)
                    print(str(getattr(player, week_data_var).total_points) + ' - ' +
                          str(getattr(player, week_data_var).total_points_against) + ' (' +
                          str(getattr(player, week_data_var).total_points -
                              getattr(player, week_data_var).total_points_against) + ')')
                    print('$' + str(getattr(player, week_data_var).money_won) + '\n')
                print('\n\n')

            else:
                print('\n\n' + player_dict[player].name + '\n')
                for team in (getattr(player_dict[player], week_data_var)).team_data:
                    print(team.name + "  ->  " + str(team.points) + "-" + str(team.points_against) + "\n")
                print("Record          ->  " + getattr(player_dict[player], week_data_var).record)
                print("Total Offense   ->  " + str(getattr(player_dict[player], week_data_var).total_points))
                print("Total Defense   ->  " + str(getattr(player_dict[player], week_data_var).total_points_against))
                print("Differential    ->  " + str(getattr(player_dict[player], week_data_var).differential))
                print("Money Won       ->  $" + str(getattr(player_dict[player], week_data_var).money_won) + '\n\n\n')


if __name__ == "__main__":
    main()