# https://adventofcode.com/2023/day/08

from utils import get_input

# Part 1

def part1(instructions, nodes):
    curr = "AAA"
    instr_idx = 0
    steps = 0
    while curr != "ZZZ":
        if instructions[instr_idx] == "R":
            curr = nodes[curr][1]
        elif instructions[instr_idx] == "L":
            curr = nodes[curr][0]
        instr_idx = (instr_idx + 1) % len(instructions)
        steps += 1
    return steps

# Part 2

def part2(instructions, nodes_dict):
    curr_nodes = curr_nodes = [node for node in nodes_dict if node.endswith("A")]

    def finish_node(start):
        curr = start
        instr_idx = 0
        steps = 0
        while not curr.endswith("Z"):
            if instructions[instr_idx] == "R":
                curr = nodes_dict[curr][1]
            elif instructions[instr_idx] == "L":
                curr = nodes_dict[curr][0]
            instr_idx = (instr_idx + 1) % len(instructions)
            steps += 1
        return steps
    
    steps_for_each = [finish_node(node) for node in curr_nodes]

    # find the LCM of all of the steps
    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    
    def find_lcm(steps):
        lcm_val = steps[0]
        for i in range(1, len(steps)):
            lcm_val = lcm(lcm_val, steps[i])
        return lcm_val
    
    return find_lcm(steps_for_each)

# -------- MAIN FUNCTION -------- #
def main():
    lines = get_input()
    instructions = lines[0]
    nodes = lines[2:]

    # for part 2, note all of the nodes that end with A and Z
    A_idxs, Z_idxs = [], []
    for idx, node in enumerate(nodes):
        if node.split(" = ")[0].endswith("A"):
            A_idxs.append(idx)
        elif node.split(" = ")[0].endswith("Z"):
            Z_idxs.append(idx)
    print(A_idxs, Z_idxs)

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
