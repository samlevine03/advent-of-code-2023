from utils import get_input, input_to_2d_array

"""
--- Day 10: Pipe Maze ---

You use the hang glider to ride the hot air from Desert Island all the way up to the floating metal island. This island is surprisingly cold and there definitely aren't any thermals to glide on, so you leave your hang glider behind.

You wander around for a while, but you don't find any people or animals. However, you do occasionally find signposts labeled " Hot Springs " pointing in a seemingly consistent direction; maybe you can find someone at the hot springs and ask them where the desert-machine parts are made.

The landscape here is alien; even the flowers and trees are made of metal. As you stop to admire some metal grass, you notice something metallic scurry away in your peripheral vision and jump into a big pipe! It didn't look like any animal you've ever seen; if you want a better look, you'll need to get ahead of it.

Scanning the area, you discover that the entire field you're standing on is densely packed with pipes ; it was hard to tell at first because they're the same metallic silver color as the "ground". You make a quick sketch of all of the surface pipes you can see (your puzzle input).

The pipes are arranged in a two-dimensional grid of *tiles* :

 - `|` is a *vertical pipe* connecting north and south.
 - `-` is a *horizontal pipe* connecting east and west.
 - `L` is a *90-degree bend* connecting north and east.
 - `J` is a *90-degree bend* connecting north and west.
 - `7` is a *90-degree bend* connecting south and west.
 - `F` is a *90-degree bend* connecting south and east.
 - `.` is *ground* ; there is no pipe in this tile.
 - `S` is the *starting position* of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

Based on the acoustics of the animal's scurrying, you're confident the pipe that contains the animal is *one large, continuous loop* .

For example, here is a square loop of pipe:

```
.....
.F-7.
.|.|.
.L-J.
.....
```

If the animal had entered this loop in the northwest corner, the sketch would instead look like this:

```
.....
.S-7.
.|.|.
.L-J.
.....
```

In the above diagram, the `S` tile is still a 90-degree `F` bend: you can tell because of how the adjacent pipes connect to it.

Unfortunately, there are also many pipes that *aren't connected to the loop* ! This sketch shows the same loop as above:

```
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
```

In the above diagram, you can still figure out which pipes form the main loop: they're the ones connected to `S` , pipes those pipes connect to, pipes *those* pipes connect to, and so on. Every pipe in the main loop connects to its two neighbors (including `S` , which will have exactly two pipes connecting to it, and which is assumed to connect back to those two pipes).

Here is a sketch that contains a slightly more complex main loop:

```
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
```

Here's the same example sketch with the extra, non-main-loop pipe tiles also shown:

```
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
```

If you want to *get out ahead of the animal* , you should find the tile in the loop that is *farthest* from the starting position. Because the animal is in the pipe, it doesn't make sense to measure this by direct distance. Instead, you need to find the tile that would take the longest number of steps *along the loop* to reach from the starting point - regardless of which way around the loop the animal went.

In the first example with the square loop:

```
.....
.S-7.
.|.|.
.L-J.
.....
```

You can count the distance each tile in the loop is from the starting point like this:

```
.....
.012.
.1.3.
.234.
.....
```

In this example, the farthest point from the start is `*4*` steps away.

Here's the more complex loop again:

```
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
```

Here are the distances for each tile on that loop:

```
..45.
.236.
01.7814567
23...
```

Find the single giant loop starting at `S` . *How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?*
"""
    

def traverse(arr):
    """
    Traverse the array and return the number of steps it takes to get from the starting position to the point farthest from the starting position.
    """

    dirs = (
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0)
    )

    def find_start(arr):
        """
        Find the starting position of the animal.
        """
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == 'S':
                    return (i, j)


    def get_starting_dir(arr, i, j):
        """
        Get the starting direction of the animal.
        """
        for d in range(len(dirs)):
            dir = dirs[d]
            if i + dir[0] < 0 or i + dir[0] >= len(arr):
                continue
            if j + dir[1] < 0 or j + dir[1] >= len(arr[i]):
                continue
            pipe = arr[i + dir[0]][j + dir[1]]
            if dir == (0, -1) and pipe in 'L-F':
                return dir
            if dir == (0, 1) and pipe in 'J-7':
                return dir
            if dir == (-1, 0) and pipe in '7|F':
                return dir
            if dir == (1, 0) and pipe in 'J|L':
                return dir
            
        return None


    start = find_start(arr)
    i, j = start

    prev_dir = None
    next_dir = get_starting_dir(arr, i, j)

    loop = ['S']
    i += next_dir[0]
    j += next_dir[1]

    while arr[i][j] != 'S':
        pipe = arr[i][j]
        loop.append(pipe)
        prev_dir = next_dir
        if pipe == '|' or pipe == '-':
            next_dir = prev_dir
        elif pipe == 'L':
            if prev_dir == (0, -1):
                next_dir = (-1, 0)
            elif prev_dir == (1, 0):
                next_dir = (0, 1)
        elif pipe == 'J':
            if prev_dir == (0, 1):
                next_dir = (-1, 0)
            elif prev_dir == (1, 0):
                next_dir = (0, -1)
        elif pipe == '7':
            if prev_dir == (0, 1):
                next_dir = (1, 0)
            elif prev_dir == (-1, 0):
                next_dir = (0, -1)
        elif pipe == 'F':
            if prev_dir == (0, -1):
                next_dir = (1, 0)
            elif prev_dir == (-1, 0):
                next_dir = (0, 1)
        i += next_dir[0]
        j += next_dir[1]

    return len(loop) // 2


"""
--- Part Two ---

You quickly reach the farthest point of the loop, but the animal never emerges. Maybe its nest is within the area enclosed by the loop?

To determine whether it's even worth taking the time to search for such a nest, you should calculate how many tiles are contained within the loop. For example:

...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........

The above loop encloses merely four tiles - the two pairs of . in the southwest and southeast (marked I below). The middle . tiles (marked O below) are not in the loop. Here is the same loop again with those regions marked:

...........
.S-------7.
.|F-----7|.
.||OOOOO||.
.||OOOOO||.
.|L-7OF-J|.
.|II|O|II|.
.L--JOL--J.
.....O.....

In fact, there doesn't even need to be a full tile path to the outside for tiles to count as outside the loop - squeezing between pipes is also allowed! Here, I is still within the loop and O is still outside the loop:

..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........

In both of the above examples, 4 tiles are enclosed by the loop.

Here's a larger example:

.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...

The above sketch has many random bits of ground, some of which are in the loop (I) and some of which are outside it (O):

OF----7F7F7F7F-7OOOO
O|F--7||||||||FJOOOO
O||OFJ||||||||L7OOOO
FJL7L7LJLJ||LJIL-7OO
L--JOL7IIILJS7F-7L7O
OOOOF-JIIF7FJ|L7L7L7
OOOOL7IF7||L7|IL7L7|
OOOOO|FJLJ|FJ|F7|OLJ
OOOOFJL-7O||O||||OOO
OOOOL---JOLJOLJLJOOO

In this larger example, 8 tiles are enclosed by the loop.

Any tile that isn't part of the main loop can count as being enclosed by the loop. Here's another example with many bits of junk pipe lying around that aren't connected to the main loop at all:

FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L

Here are just the tiles that are enclosed by the loop marked with I:

FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJIF7FJ-
L---JF-JLJIIIIFJLJJ7
|F|F-JF---7IIIL7L|7|
|FFJF7L7F-JF7IIL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L

In this last example, 10 tiles are enclosed by the loop.

Figure out whether you have time to search for the nest by calculating the area within the loop. How many tiles are enclosed by the loop?
"""

def traverse_2(arr):
    """
    Traverse the array and return the number of steps it takes to get from the starting position to the point farthest from the starting position.
    """

    dirs = (
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0)
    )

    def find_start(arr):
        """
        Find the starting position of the animal.
        """
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == 'S':
                    return (i, j)


    def get_starting_dir(arr, i, j):
        """
        Get the starting direction of the animal.
        """
        for d in range(len(dirs)):
            dir = dirs[d]
            if i + dir[0] < 0 or i + dir[0] >= len(arr):
                continue
            if j + dir[1] < 0 or j + dir[1] >= len(arr[i]):
                continue
            pipe = arr[i + dir[0]][j + dir[1]]
            if dir == (0, -1) and pipe in 'L-F':
                return dir
            if dir == (0, 1) and pipe in 'J-7':
                return dir
            if dir == (-1, 0) and pipe in '7|F':
                return dir
            if dir == (1, 0) and pipe in 'J|L':
                return dir
            
        return None


    start = find_start(arr)
    i, j = start

    prev_dir = None
    next_dir = get_starting_dir(arr, i, j)

    loop = ['S']
    loop_coords = set()
    loop_coords.add((i, j))
    i += next_dir[0]
    j += next_dir[1]

    while arr[i][j] != 'S':
        pipe = arr[i][j]
        loop.append(pipe)
        loop_coords.add((i, j))
        prev_dir = next_dir
        if pipe == '|' or pipe == '-':
            next_dir = prev_dir
        elif pipe == 'L':
            if prev_dir == (0, -1):
                next_dir = (-1, 0)
            elif prev_dir == (1, 0):
                next_dir = (0, 1)
        elif pipe == 'J':
            if prev_dir == (0, 1):
                next_dir = (-1, 0)
            elif prev_dir == (1, 0):
                next_dir = (0, -1)
        elif pipe == '7':
            if prev_dir == (0, 1):
                next_dir = (1, 0)
            elif prev_dir == (-1, 0):
                next_dir = (0, -1)
        elif pipe == 'F':
            if prev_dir == (0, -1):
                next_dir = (1, 0)
            elif prev_dir == (-1, 0):
                next_dir = (0, 1)
        i += next_dir[0]
        j += next_dir[1]

    return loop_coords


def count_enclosed_tiles(arr, loop_coords):

    def enclosed(i, j):
        count = 0
        for k in range(j):
            if not (i, k) in loop_coords:
                continue
            if arr[i][k] in "F7|":  # note, using JL instead of 7F didn't work since the S is a J!
                count += 1
        
        if count % 2 != 0:
            return True
        
        return False
        
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if not (i, j) in loop_coords:
                if enclosed(i, j):
                    count += 1

    return count




# -------- MAIN FUNCTION -------- #
def main():
    lines = get_input()
    arr = input_to_2d_array(lines)
    part1 = traverse(arr)
    print(f'Part 1: {part1}')

    loop_coords = traverse_2(arr)
    part2 = count_enclosed_tiles(arr, loop_coords)
    print(f'Part 2: {part2}')


if __name__ == "__main__":
    main()
