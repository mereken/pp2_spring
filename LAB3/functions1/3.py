def solve (numheads, numlegs):
    rab = numlegs / 2 - numheads
    chick = numheads - rab
    return int(rab), int(chick)
numheads = int(input(" number of heads: "))
numlegs = int(input(" number of legs: "))
print(solve(numheads, numlegs))