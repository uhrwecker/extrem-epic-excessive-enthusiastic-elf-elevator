from Classes.Playerc import playerclass as pc

player_1 = pc.player('human', 'mage')
player_2 = pc.player('orc', 'fighter')

player_1.change_stat("HP", 1)

print(player_1.HP)

print("Player 1:","\n", player_1.stat_display())
print("Player 2:","\n", player_2.stat_display())