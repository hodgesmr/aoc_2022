import operator
from collections import deque

from utils import get_input_lines, timed


# A Node represents a file / directory
class Node:
    def __init__(self, name, weight=0):
        self.children = []
        self.name = name
        self.weight = weight

    @property
    def total_weight(self):
        return self.weight + sum(child.total_weight for child in self.children)


# Walk the input line by line
# Build out our file_system graph
# Use a deque (stack) to keep track of where we are and where we came from
def build_file_system(input):
    file_system = None
    cwd = deque()
    for line in input:
        line_parts = line.split(" ")
        if line[0] == "$":  # an input command
            command = line_parts[1]
            if command == "cd":  # a cd command
                dir_name = line_parts[2]
                if dir_name == "..":  # Go back up
                    cwd.pop()
                else:
                    if file_system:  # We're going down a dir
                        next_subdir = next(  # Find the child Node that matches the typed name
                            (
                                subdir
                                for subdir in file_system.children
                                if subdir.name == dir_name
                            )
                        )
                    else:  # This only hits once when we initialize '/'
                        next_subdir = Node(dir_name)
                    cwd.append(next_subdir)  # Add the cd'd dir to the stack

                file_system = cwd[-1]  # Orient our "root" at the top of the stack
        else:  # This is the output of `ls`
            try:  # Add a file child if the first value is a file size
                file_size = int(line_parts[0])
                file_system.children.append(Node(line_parts[1], file_size))
            except ValueError:  # add a dir child
                file_system.children.append(Node(line_parts[1]))

    while cwd:  # pop all the way back to root
        file_system = cwd.pop()

    return file_system


# This is DFS
# Drill down through the file system
# Return a set of dirs that meet a threshold value (size) for an operator (<, >=, etc)
def find_directories_meeting_threshold(visited, visited_threshold, op, threshold, node):
    if node not in visited:
        visited.add(node)  # track everything we've seen
        if node.children and op(node.total_weight, threshold):  # it has children, it's a dir
            visited_threshold.add(node)  # track everything that meets our threshold
        for child in node.children:
            find_directories_meeting_threshold(  # ✨ Recursion ✨
                visited, visited_threshold, op, threshold, child
            )



# Build the file system
# Find all the dirs less than 100000
# Sum those dir sizes up, and return
def part_1(input):
    file_system = build_file_system(input)

    visited = set()
    visited_threshold = set()
    target = 100000

    find_directories_meeting_threshold(
        visited, visited_threshold, operator.lt, target, file_system
    )

    return sum(v.total_weight for v in visited_threshold)


# Build the file system
# Find all the dirs greater than our needed space
# Return the smallest of those
def part_2(input):
    file_system = build_file_system(input)

    disk = 70000000
    used = file_system.total_weight
    free = disk - used
    need = 30000000
    to_find = need - free

    visited = set()
    visited_threshold = set()

    find_directories_meeting_threshold(
        visited, visited_threshold, operator.ge, to_find, file_system
    )

    return min(v.total_weight for v in visited_threshold)


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
