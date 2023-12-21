# https://adventofcode.com/2023/day/08

from utils import get_input
from math import gcd
from functools import reduce

# Part 1

def part1(instructions, nodes):
    curr, instr_idx, steps = "AAA", 0, 0
    while curr != "ZZZ":
        curr = nodes[curr][0 if instructions[instr_idx] == "L" else 1]
        instr_idx = (instr_idx + 1) % len(instructions)
        steps += 1
    return steps

# Part 2

def part2(instructions, nodes_dict):
    curr_nodes = [node for node in nodes_dict if node.endswith("A")]

    def finish_node(start):
        curr, instr_idx, steps = start, 0, 0
        while not curr.endswith("Z"):
            curr = nodes_dict[curr][0 if instructions[instr_idx] == "L" else 1]
            instr_idx = (instr_idx + 1) % len(instructions)
            steps += 1
        return steps
    
    steps_for_each = [finish_node(node) for node in curr_nodes]
    return reduce(lambda a, b: (a * b) // gcd(a, b), steps_for_each)

# -------- MAIN FUNCTION -------- #
def main():
    lines = get_input()
    instructions = lines[0]
    nodes = lines[2:]
    nodes_dict = {node.split(" = ")[0]: node.split(" = ")[1].replace("(", "").replace(")", "").split(", ") for node in nodes}
    
    num_steps = part1(instructions, nodes_dict)
    print(f"Part 1: {num_steps}")

    # quick explanation, cuz this was a total shot in the dark
    # i basically just guessed that for any respective start node, it would just have one
    # corresponding end node, and it would just continously go through the loop traveling between them
    # so i just found the number of steps it took to get from each start node to its end node, and then 
    # found the LCM of all of those steps

    num_steps = part2(instructions, nodes_dict)
    print(f"Part 2: {num_steps}")

if __name__ == "__main__":
    main()
