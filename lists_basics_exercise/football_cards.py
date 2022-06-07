a_team_players = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10"]
b_team_players = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10"]
game_over = False
sent_off_players = input().split()
len_a = 0
len_b = 0
for player in sent_off_players:
    if player in a_team_players:
        a_team_players.remove(player)
        if len(a_team_players)<6:
            len_a = len(a_team_players)-1
            game_over = True
            break
    elif player in b_team_players:
        b_team_players.remove(player)
        if len(b_team_players)<6:
            len_b = len(b_team_players)-1
            game_over = True
            break
print(f'Team A - {len(a_team_players)+1}; Team B - {len(b_team_players)+1}')
if game_over:
    print(f'Game was terminated')