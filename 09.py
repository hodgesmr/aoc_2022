from utils import get_input_lines, timed

import math


class Knot():
    def __init__(self):
        self.location = (0, 0)
        self.history = [self.location]

    def move_euclidean(self, direction):
        # parse the input
        if direction == 'U' or direction == 'D':
            c_index = 1
        else:
            c_index = 0

        if direction == 'U' or direction == 'R':
            c_delta = 1
        else:
            c_delta = -1

        # some of this cruft is because tuples are immutable
        new_location = [0, 0]
        for i in range(c_index-1, c_index+1):
            if i == c_index:
                new_location[i] = self.location[c_index] + c_delta
            else:
                new_location[i] = self.location[(c_index-1)]

        # update location and add to history
        self.location = tuple(new_location)
        self.history.append(self.location)


    def move_free(self, other_knot):
        x = self.location[0]
        y = self.location[1]

        x_gap = other_knot.location[0] - x
        y_gap = other_knot.location[1] - y
        
        # We only have to do one move, because we will never be more than 2 away
        if x_gap > 0:
            x += 1
        elif x_gap < 0:
            x -= 1

        if y_gap > 0:
            y += 1
        elif y_gap < 0:
            y -= 1

        self.location = (x, y)
        self.history.append(self.location)
        

    def touching(self, other_knot):
        distance = math.dist(self.location, other_knot.location)
        return distance < 2



def part_1(input):
    head = Knot()
    tail = Knot()

    for move in input:
        direction, distance = move.split(' ')

        for _ in range(int(distance)):
            head.move_euclidean(direction)  # update head
            if not tail.touching(head):  # update tail
                tail.move_free(head)

    return len(set(tail.history))  # return the unique coords in the history
        

def part_2(input):
    knots = [Knot() for k in range(10)]
    for move in input:
        direction, distance = move.split(' ')

        for _ in range(int(distance)):
            knots[0].move_euclidean(direction)  # update head
            for i in range(1, 10):  # update all the other knots in the chain
                knot = knots[i]
                leader = knots[i-1]
                if not knot.touching(leader):
                    knot.move_free(leader)

    return len(set(knots[-1].history))  # return the unique coords in the history


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
