def collision_detect(box1, box2):
    side_left1 = box1.x
    side_right1 = box1.x + box1.x_length
    side_top1 = box1.y
    side_bottom1 = box1.y + box1.y_length

    side_left2 = box2.x
    side_right2 = box2.x + box2.x_length
    side_top2 = box2.y
    side_bottom2 = box2.y + box2.y_length

    if side_right1 > side_left2 > side_left1 or side_right1 > side_right2 > side_left1 or (side_right1 == side_right2 and side_left1 == side_left2):  # are x sides of box1 in box2
        if side_bottom1 > side_top2 > side_top1 or side_bottom1 > side_bottom2 > side_top1 or (side_bottom1 == side_bottom2 and side_top1 == side_top2):  # ^ but for y sides
            return True
    if side_right2 > side_left1 > side_left2 or side_right2 > side_right1 > side_left2:  # are x sides of box2 in box1
        if side_bottom2 > side_top1 > side_top2 or side_bottom2 > side_bottom1 > side_top2:  # ^ but for y sides
            return True


def collision_resolve(player, entity):
    player_x1 = player.x_past
    player_x2 = player.x
    player_y1 = player.y_past
    player_y2 = player.y

    entity_pos = (entity.x, entity.y)

    delta_y = player_y2 - player_y1  # calculating change in x and y
    delta_x = player_x2 - player_x1

    if delta_y > 0:  # calculates the step direction for resolution for loop
        loop_delta_y = 1
    else:
        loop_delta_y = -1  # defaults to -1, but doesn't matter, only used in event of motion

    if delta_x > 0:
        loop_delta_x = 1
    else:
        loop_delta_x = -1

    print(delta_y, loop_delta_y)

    if not delta_x and not delta_y:  # if there is not x or y change, the player isn't moving
        print("No motion")


    elif not delta_x and delta_y:  # if there is no change in x, the player is moving only on y axis
        print("X =", player_x1)

        list = []

        # for loop from 3 to 5 will only loop through 3 to 4, 1 needs to be added in the appropriate direction
        # step number is either +1 or -1 depending on the loop_delta value
        for i in range(player_y1, player_y2 + loop_delta_y, loop_delta_y):
            list.append(i)

        print(list)


    elif delta_x and not delta_y:  # if there is no change in y, the player is moving only on x axis
        print("Y =", player_y1)


    else:  # if there is a change in x and y, the linear equation is found
        slope = delta_y / delta_x
        intercept = player_x1 - player_y1 * slope
        print("y = " + str(round(slope, 3)) + "x + " + str(round(intercept, 3)))

