player_pos1 = (4, 3)
player_pos2 = (8, 5)
player_len = 6

entity_pos = (13, 11)
entity_pos2 = (entity_pos[0] + player_len, entity_pos[1] + player_len)

slope = (player_pos1[1] - player_pos2[1]) / (player_pos1[0] - player_pos2[0])  # calculates slope based on two points
intercept = player_pos1[1] - player_pos1[0] * slope  # calculates y intercept for linear equation

print(entity_pos, entity_pos2)

print("y = " + str(round(slope, 3)) + "x + " + str(round(intercept, 3)))  # prints out linear equation

for i in range(player_pos1[0], player_pos2[0] + 1):  # runs through all x positions from the first to second point
    y = slope * i + intercept  # calculates corresponding y value for each x value in the loop
    coords = ((i, round(y)), (i + player_len, round(y)), (i, round(y + player_len)), (i+ player_len, round(y + player_len)))
    # calculates the points of the 4 corners of the hitbox and puts them into a tuple for further analysis

    for j in coords:  # runs through the generated four points of each x position
        print(j)
        if j[0] == (entity_pos[0] or entity_pos2[0]) and entity_pos[1] <= j[1] <= entity_pos2[1]:
            print("---", j, " x", (i, round(y)))
            break
        if j[1] == (entity_pos[1] or entity_pos2[1]) and entity_pos[0] <= j[0] <= entity_pos2[0]:
            print(entity_pos[1], entity_pos2[1])
            print("---", j, " y", (i, round(y)))
            break


