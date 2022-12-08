from utils import get_input_lines, timed


# I'm really not happy with this answer
# I believe I could do this O(n) if I walked the grid in a smart way
# Instead, I look at each tree and then look in all 4 directions
# This results in a ton of re-evaluation of trees in the cross hairs
# At least the code is brief, I suppose.
def part_1(input):
    grid = [list(line) for line in input]
    visible = 2*len(grid[0]) + 2*(len(grid)-2)  # edges are visible
    for i in range(1, len(grid) -1):  # loop over the internal rows
        for j in range(1, len(grid[0]) - 1):  # loop over the interal cols

            # at least short-circuiting will save us from doing some of these walks
            if (all(grid[i][k] < grid[i][j] for k in range(j + 1, len(grid[i]))) or  # Check left
                all(grid[i][k] < grid[i][j] for k in range(0, j)) or  # Check right
                all(grid[k][j] < grid[i][j] for k in range(0, i)) or  # Check up
                all(grid[k][j] < grid[i][j] for k in range(i + 1, len(grid)))  # Check down
            ):
                visible += 1
    return visible



# For each tree in the grid,
# walk in all 4 directions until you hit a tree that obstructs your view
# Count as you go
# Multiply the 4 values
def part_2(input):
    grid = [list(line) for line in input]
    scores = set()

    for row_idx, row in enumerate(grid):
        for col, me in enumerate(row):
            
            # walk left
            left_score = 0
            leftward_idx = col-1
            left_calculated = False
            while not left_calculated and leftward_idx >= 0:
                left_tree = row[leftward_idx]
                if left_tree <= me:
                    left_score += 1
                if left_tree >= me:
                    left_calculated = True
                leftward_idx -= 1

            # walk right
            right_score = 0
            rightward_idx = col+1
            right_calculated = False
            while not right_calculated and rightward_idx < len(row):
                right_tree = row[rightward_idx]
                if right_tree <= me:
                    right_score += 1
                if right_tree >= me:
                    right_calculated = True
                rightward_idx += 1

            # walk up
            up_score = 0
            upward_idx = row_idx-1
            up_calculated = False
            while not up_calculated and upward_idx >= 0:
                up_tree = grid[upward_idx][col]
                if up_tree <= me:
                    up_score += 1
                if up_tree >= me:
                    up_calculated = True
                upward_idx -= 1

            # walk down
            down_score = 0
            downward_idx = row_idx+1
            down_calculated = False
            while not down_calculated and downward_idx < len(grid):
                down_tree = grid[downward_idx][col]
                if down_tree <= me:
                    down_score += 1
                if down_tree >= me:
                    down_calculated = True
                downward_idx += 1

            scores.add((left_score * right_score * up_score * down_score))

    return max(scores)


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
