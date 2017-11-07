player_pos1 = (4, 2)
player_pos2 = (7, 4)
player_len = 6

entity_pos = (6, 9)

slope = (player_pos1[1] - player_pos2[1]) / (player_pos1[0] - player_pos2[0])

intercept = player_pos1[1] - player_pos1[0] * slope

print("y = " + str(round(slope, 3)) + "x + " + str(round(intercept, 3)))

for i in range(player_pos1[0], player_pos2[0] + 1):
    y = slope * i + intercept
    coords = ((i, y), (i + player_len, y), (i, y + player_len), (i+ player_len, y + player_len))

    for j in coords:
        if j[0] == (entity_pos[0] or entity_pos[0] + player_len):
            print(j, " x", (i, round(y)))
        if j[1] == (entity_pos[1] or entity_pos[1] + player_len):
            print(j, " y")


