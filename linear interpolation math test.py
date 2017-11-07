player_pos1 = (11, 5)
player_pos2 = (3, 2)
player_len = 6

entity_pos = (1, 1)
entity_pos2 = (entity_pos[0] + player_len, entity_pos[1] + player_len)

slope = (player_pos1[1] - player_pos2[1]) / (player_pos1[0] - player_pos2[0])  # calculates slope based on two points
intercept = player_pos1[1] - player_pos1[0] * slope  # calculates y intercept for linear equation

print(entity_pos, entity_pos2)

print("y = " + str(round(slope, 3)) + "x + " + str(round(intercept, 3)))  # prints out linear equation

end_loop = False

if player_pos1[0] < player_pos2[0]:
    loop_change = 1
else:
    loop_change = -1

for i in range(player_pos1[0], player_pos2[0] + 1, loop_change):  # runs through all x positions from the first to second point
    if end_loop:
        break
    y = slope * i + intercept  # calculates corresponding y value for each x value in the loop
    coords = ((i, y), (i + player_len, y), (i, y + player_len), (i+ player_len, y + player_len))
    # calculates the points of the 4 corners of the hitbox and puts them into a tuple for further analysis

    for j in coords:  # runs through the generated four points of each x position
        x = round(j[0])
        y = round(j[1])
        if x == entity_pos[0] or x == entity_pos2[0] and entity_pos[1] <= x <= entity_pos2[1]:
            print("---", j, " x", (i, round(y)))
            end_loop = True
            break
        if y == entity_pos[1] or y == entity_pos2[1] and entity_pos[0] <= y <= entity_pos2[0]:
            print("---", j, " y", (i, round(y)))
            end_loop = True
            break


