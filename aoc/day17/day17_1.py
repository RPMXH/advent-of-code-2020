workspace = [["..##.##..", "#.#..###.", "##.#.#.#.", "#.#.##.#.", "###..#...", ".#.#..##.", "#.##.###.", "#.#..##..",
              "........."]]

# workspace = [[".#.", "..#", "###"]]
center_xy_location = int((len(workspace[0]) - 1) / 2)
center_z_location = 0

active_status = '#'
inactive_status = '.'


def enlarge_xy_workspace():
    global future_center_xy_location
    global future_workspace

    future_center_xy_location += 1
    new_workspace = []

    for z_layer in future_workspace:
        new_z_layer = []
        new_z_layer.append(inactive_status * (future_center_xy_location * 2 + 1))
        for y_row in z_layer:
            new_z_layer.append(inactive_status + y_row[:] + inactive_status)
        new_z_layer.append(inactive_status * (future_center_xy_location * 2 + 1))

        new_workspace.append(new_z_layer[:])

    future_workspace = []
    for z_layer in new_workspace:
        future_workspace.append(z_layer[:])


def enlarge_z_workspace():
    global future_center_z_location
    global future_workspace

    future_center_z_location += 1
    new_workspace = []

    new_layer = [inactive_status * (future_center_xy_location * 2 + 1)] * (future_center_xy_location * 2 + 1)
    new_workspace.append(new_layer[:])
    for z_layer in future_workspace:
        new_workspace.append(z_layer[:])

    new_workspace.append(new_layer[:])

    future_workspace = []
    for z_layer in new_workspace:
        future_workspace.append(z_layer[:])


def set_location_status(diff_x, diff_y, diff_z, status):
    global future_center_xy_location
    global future_center_z_location
    global future_workspace

    real_x = future_center_xy_location + diff_x
    real_y = future_center_xy_location + diff_y
    if real_x < 0 or real_x >= len(future_workspace[0]) or real_y < 0 or real_y >= len(future_workspace[0]):
        enlarge_xy_workspace()
        real_x = future_center_xy_location + diff_x
        real_y = future_center_xy_location + diff_y

    real_z = future_center_z_location + diff_z
    if real_z < 0 or real_z >= len(future_workspace):
        enlarge_z_workspace()
        real_z = future_center_z_location + diff_z

    future_row = future_workspace[real_z][real_y][:real_x] + status + future_workspace[real_z][real_y][(real_x + 1):]
    future_workspace[real_z][real_y] = future_row


def get_location_status(diff_x, diff_y, diff_z):
    global center_xy_location
    global center_z_location
    global workspace

    real_x = center_xy_location + diff_x
    if real_x < 0 or real_x >= len(workspace[0]):
        return inactive_status

    real_y = center_xy_location + diff_y
    if real_y < 0 or real_y >= len(workspace[0]):
        return inactive_status

    real_z = center_z_location + diff_z
    if real_z < 0 or real_z >= len(workspace):
        return inactive_status

    return workspace[real_z][real_y][real_x]


def is_location_active(x, y, z):
    if get_location_status(x, y, z) == '#':
        return 1

    return 0


def count_active_neighbours(x0, y0, z0):
    count = 0
    neighbour_positions = [-1, 0, 1]
    for z in neighbour_positions:
        for y in neighbour_positions:
            for x in neighbour_positions:
                if z != 0 or y != 0 or x != 0:
                    count += is_location_active(x + x0, y + y0, z + z0)

    return count


def get_location_future_status(x, y, z, current_status):
    neighbour_count = count_active_neighbours(x, y, z)
    if current_status == active_status:
        if 2 <= neighbour_count <= 3:
            return active_status
        else:
            return inactive_status
    elif current_status == inactive_status:
        if neighbour_count == 3:
            return active_status
        else:
            return inactive_status


def cycle():
    global center_xy_location
    global center_z_location
    global workspace
    global future_center_xy_location
    global future_center_z_location
    global future_workspace

    future_workspace = []
    for z_layer in workspace:
        future_workspace.append(z_layer[:])

    future_center_xy_location = center_xy_location
    future_center_z_location = center_z_location

    range_xy = center_xy_location + 1
    range_z = center_z_location + 1

    for z in range(-range_z, range_z + 1):
        for y in range(-range_xy, range_xy + 1):
            for x in range(-range_xy, range_xy + 1):
                current_status = get_location_status(x, y, z)
                future_status = get_location_future_status(x, y, z, current_status)
                if current_status != future_status:
                    set_location_status(x, y, z, future_status)

    workspace = []
    for z_layer in future_workspace:
        workspace.append(z_layer[:])

    center_xy_location = future_center_xy_location
    center_z_location = future_center_z_location


def count_all_active():
    global workspace

    count = 0
    for z_layer in workspace:
        for y_row in z_layer:
            for x_char in y_row:
                if x_char == active_status:
                    count += 1

    return count


def display_workspace():
    for z_index, z_layer in enumerate(workspace, start=0):
        print("\nlayer " + str(z_index - center_z_location))
        for y_row in z_layer:
            print(y_row)


##################### PRESENTATION ######################


display_workspace()
print("\n0th round")
print(count_all_active())

for i in range(6):
    cycle()

    display_workspace()
    print("\n" + str(i + 1) + "th round")
    print(count_all_active())

exit(0)
