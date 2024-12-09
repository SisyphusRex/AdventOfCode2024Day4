def main(*args):
    """main method"""
    maze = read_maze("data.txt")
    find_xmas(maze)
    find_mas(maze)


def find_mas(maze):
    count = 0
    for y_index, row in enumerate(maze):
        for x_index, value in enumerate(row):
            if value == "A":
                if check_m_top(maze, x_index, y_index):
                    count += 1
                if check_m_right(maze, x_index, y_index):
                    count += 1
                if check_m_bottom(maze, x_index, y_index):
                    count += 1
                if check_m_left(maze, x_index, y_index):
                    count += 1

    print(f"part2: {count}")


def check_m_top(maze, x_index, y_index):
    try:
        if maze[y_index - 1][x_index - 1] == "M":
            if (y_index - 1) < 0:
                return False
            if (x_index - 1) < 0:
                return False
            if maze[y_index - 1][x_index + 1] == "M":
                if maze[y_index + 1][x_index - 1] == "S":
                    if maze[y_index + 1][x_index + 1] == "S":
                        return True
        return False
    except IndexError:
        return False


def check_m_right(maze, x_index, y_index):
    try:
        if maze[y_index - 1][x_index + 1] == "M":
            if (y_index - 1) < 0:
                return False
            if (x_index - 1) < 0:
                return False
            if maze[y_index + 1][x_index + 1] == "M":
                if maze[y_index + 1][x_index - 1] == "S":
                    if maze[y_index - 1][x_index - 1] == "S":
                        return True
        return False
    except IndexError:
        return False


def check_m_bottom(maze, x_index, y_index):
    try:
        if maze[y_index + 1][x_index + 1] == "M":
            if (y_index - 1) < 0:
                return False
            if (x_index - 1) < 0:
                return False
            if maze[y_index + 1][x_index - 1] == "M":
                if maze[y_index - 1][x_index - 1] == "S":
                    if maze[y_index - 1][x_index + 1] == "S":
                        return True
        return False
    except IndexError:
        return False


def check_m_left(maze, x_index, y_index):
    try:
        if maze[y_index + 1][x_index - 1] == "M":
            if (y_index - 1) < 0:
                return False
            if (x_index - 1) < 0:
                return False
            if maze[y_index - 1][x_index - 1] == "M":
                if maze[y_index - 1][x_index + 1] == "S":
                    if maze[y_index + 1][x_index + 1] == "S":
                        return True
        return False
    except IndexError:
        return False


def find_xmas(maze):
    count = 0
    for y_index, row in enumerate(maze):
        for x_index, value in enumerate(row):
            if value == "X":
                if check_horizontal_forwards(maze, x_index, y_index):
                    count += 1
                if check_horizontal_backwards(maze, x_index, y_index):
                    count += 1
                if check_vertical_forwards(maze, x_index, y_index):
                    count += 1
                if check_vertical_backwards(maze, x_index, y_index):
                    count += 1
                if check_diagonal_down_right(maze, x_index, y_index):
                    count += 1
                if check_diagonal_down_left(maze, x_index, y_index):
                    count += 1
                if check_diagonal_up_left(maze, x_index, y_index):
                    count += 1
                if check_diagonal_up_right(maze, x_index, y_index):
                    count += 1

    print(f"part1: {count}")


def check_horizontal_forwards(maze, x_index, y_index):
    try:

        if maze[y_index][x_index + 1] == "M":

            if maze[y_index][x_index + 2] == "A":

                if maze[y_index][x_index + 3] == "S":
                    return True
        return False
    except IndexError:
        return False


def check_horizontal_backwards(maze, x_index, y_index):
    try:
        if maze[y_index][x_index - 1] == "M":
            if maze[y_index][x_index - 2] == "A":
                if maze[y_index][x_index - 3] == "S":
                    if (x_index - 3) < 0:
                        return False
                    return True
        return False
    except IndexError:
        return False


def check_vertical_forwards(maze, x_index, y_index):
    try:
        if maze[y_index + 1][x_index] == "M":
            if maze[y_index + 2][x_index] == "A":
                if maze[y_index + 3][x_index] == "S":
                    return True
        return False
    except IndexError:
        return False


def check_vertical_backwards(maze, x_index, y_index):
    try:
        if maze[y_index - 1][x_index] == "M":
            if maze[y_index - 2][x_index] == "A":
                if maze[y_index - 3][x_index] == "S":
                    if (y_index - 3) < 0:
                        return False
                    return True
        return False
    except IndexError:
        return False


def check_diagonal_down_right(maze, x_index, y_index):
    try:
        if maze[y_index + 1][x_index + 1] == "M":
            if maze[y_index + 2][x_index + 2] == "A":
                if maze[y_index + 3][x_index + 3] == "S":
                    return True
        return False
    except IndexError:
        return False


def check_diagonal_down_left(maze, x_index, y_index):
    try:
        if maze[y_index + 1][x_index - 1] == "M":
            if maze[y_index + 2][x_index - 2] == "A":
                if maze[y_index + 3][x_index - 3] == "S":
                    if (x_index - 3) < 0:
                        return False
                    return True
        return False
    except IndexError:
        return False


def check_diagonal_up_left(maze, x_index, y_index):
    try:
        if maze[y_index - 1][x_index - 1] == "M":
            if maze[y_index - 2][x_index - 2] == "A":
                if maze[y_index - 3][x_index - 3] == "S":
                    if (y_index - 3) < 0:
                        return False
                    if (x_index - 3) < 0:
                        return False
                    return True
        return False
    except IndexError:
        return False


def check_diagonal_up_right(maze, x_index, y_index):
    try:
        if maze[y_index - 1][x_index + 1] == "M":
            if maze[y_index - 2][x_index + 2] == "A":
                if maze[y_index - 3][x_index + 3] == "S":
                    if (y_index - 3) < 0:
                        return False
                    return True
        return False
    except IndexError:
        return False


def read_maze(filename):
    """Reads a maze from a text file and returns it as a list of lists."""
    maze = []
    with open(filename, "r") as f:
        for line in f:
            maze.append(list(line.strip()))
    return maze
