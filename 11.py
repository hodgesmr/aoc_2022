import operator
import re
from collections import deque

from utils import get_input_lines, timed


class Monkey:
    def __init__(
        self,
        modular=None,
        op=None,
        operand=None,
        true_monkey=None,
        false_monkey=None,
        worry_divisor=3,
    ):
        self.items = deque()
        self.modular = modular
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.op = op
        self.operand = operand
        self.worry_divisor = worry_divisor
        self.inspect_count = 0

    # Function to execute our operation
    def caluclate_new(self, val):
        operand = self.operand
        if not operand:
            operand = val
        new = self.op(val, operand) // self.worry_divisor
        self.inspect_count += 1  # Keep track of our inspect count
        return new

    # Function to throw to other monkeys
    def do_throws(self, monkey_list):

        # This took me a really long time to even try
        # Lots of trial and error with the mod math to get here
        # I *think* this only works because all the modular values are unique primes?
        # If we keep track of a Least Common Multiple of our modular values
        # We can keep our "worry" score in check.
        # More below...
        lcm = 1
        for m in monkey_list:
            lcm *= m.modular

        # Loop over all the items
        while self.items:
            # Get an item
            val = self.items.popleft()
            # Calculate our new value based on the worry operation
            new = self.caluclate_new(val)

            # Find out which monkey we need to throw to
            test_result = new % self.modular
            # Here's the weird LCM math
            # If we're greater than our LCM,
            # Just stay one modular tick above the lcm
            # This prevents our values from growing
            # And it keeps the same answer of who we throw to
            if new > lcm:
                remainder = new % lcm
                new = lcm + remainder

            if test_result == 0:
                monkey_list[self.true_monkey].items.append(new)
            else:
                monkey_list[self.false_monkey].items.append(new)


def build_monkey_list(input, worry_divisor):
    monkeys = []
    for line in input:
        if "Monkey" in line:
            monkeys.append(Monkey())
            monkey_index = [int(s) for s in re.findall(r"\d+", line)][-1]
        elif "Starting" in line:
            items = [int(s) for s in re.findall(r"\d+", line)]
            for item in items:
                monkeys[monkey_index].items.append(item)
        elif "Operation" in line:
            pieces = line.split("=")[1].strip().split(" ")
            if pieces[1] == "+":
                op = operator.add
            else:
                op = operator.mul
            monkeys[monkey_index].op = op

            if pieces[2] == "old":
                operand = None
            else:
                operand = int(pieces[2])
            monkeys[monkey_index].operand = operand

        elif "Test" in line:
            modular = [int(s) for s in re.findall(r"\d+", line)][-1]
            monkeys[monkey_index].modular = modular

        elif "true" in line:
            true_monkey = int(line[-1])
            monkeys[monkey_index].true_monkey = true_monkey

        elif "false" in line:
            false_monkey = int(line[-1])
            monkeys[monkey_index].false_monkey = false_monkey

        monkeys[monkey_index].worry_divisor = worry_divisor

    return monkeys


def part_1(input):
    monkeys = build_monkey_list(input, 3)

    for _ in range(20):
        for monkey in monkeys:
            monkey.do_throws(monkeys)

    inspected = sorted([m.inspect_count for m in monkeys], reverse=True)
    return inspected[0] * inspected[1]


def part_2(input):
    monkeys = build_monkey_list(input, 1)

    for _ in range(10000):
        for monkey in monkeys:
            monkey.do_throws(monkeys)

    inspected = sorted([m.inspect_count for m in monkeys], reverse=True)
    return inspected[0] * inspected[1]


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
