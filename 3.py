# This is only a helper function to see if we have a valid positino.
def is_valid_position(maze, pos_r, pos_c):
    if pos_r < 0 or pos_c < 0:
        return False
    if pos_r >= len(maze) or pos_c >= len(maze[0]):
        return False
    if maze[pos_r][pos_c] in ' x':
        return True
    return False


def print_maze(maze):
    for row in maze:
        for item in row:
            print(item, end='')
        print()


def find_start(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 'o':
                return row, col


# This is only a helper function to see if we have a valid positino.
def is_valid_position(maze, pos_r, pos_c):
    if pos_r < 0 or pos_c < 0:
        return False
    if pos_r >= len(maze) or pos_c >= len(maze[0]):
        return False
    if maze[pos_r][pos_c] in ' x':
        return True
    return False


def solve_maze(maze, start):
    # We use a Python list as a stack - then we have push operations as append, and pop as pop.
    stack = []

    # Add the entry point (as a tuple)
    stack.append(start)

    # Go through the stack as long as there are elements
    while len(stack) > 0:
        pos_r, pos_c = stack.pop()

        if maze[pos_r][pos_c] == 'x':
            print("Goal Found")
            if print_maze(maze) is not None:
                print(print_maze(maze))
            return True

        if maze[pos_r][pos_c] == '.':
            # Already visited
            continue

        # Mark position as visited
        maze[pos_r][pos_c] = '.'
        # Check for all possible positions and add if possible
        if is_valid_position(maze, pos_r - 1, pos_c):
            stack.append((pos_r - 1, pos_c))
        if is_valid_position(maze, pos_r + 1, pos_c):
            stack.append((pos_r + 1, pos_c))
        if is_valid_position(maze, pos_r, pos_c - 1):
            stack.append((pos_r, pos_c - 1))
        if is_valid_position(maze, pos_r, pos_c + 1):
            stack.append((pos_r, pos_c + 1))

    # We didn't find a path, hence we do not need to return the path
    return False


maze = "##############################\n"\
       "#         #              #   #\n"\
       "# ####    ########       #   #\n"\
       "#  o #    #              #   #\n"\
       "#    ###     #####  ######   #\n"\
       "#      #   ###   #           #\n"\
       "#      #     #   #  #  #     #\n"\
       "#     #####    #    #  # x   #\n"\
       "#              #       #     #\n"\
       "##############################"

converted_maze = []
lines = maze.splitlines()
for line in lines:
    converted_maze.append(list(line))
maze = converted_maze
start = find_start(maze)
print("Starting Point:", start)
solve_maze(maze, start)
