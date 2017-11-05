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


def collision_prevent(ent):
    x_diff = ent.x - ent.x_past
    y_diff = ent.y - ent.y_past
    change = 0

    try:
        slope = y_diff/x_diff
    except ZeroDivisionError:
        slope = 0

    yint = ent.y - (ent.x * slope)

    # range(1, 3, stepping by 1) includes values from 0 to 2, therefore 1 needs to  be added to it (vice versa for -)

    if ent.x_past <= ent.x:  # sets stepping value and adds to max of range for reason above
        change = 1
    if ent.x_past > ent.x:
        change = -1

    list = []

    for i in range(ent.x_past, ent.x + change, change):
        yval = round(i * slope + yint)
        list.append(yval)
        if yval == 400:
            ent.y = 400 - ent.y_length
    print(list)
    # print(list)
    # print(slope, yint)
