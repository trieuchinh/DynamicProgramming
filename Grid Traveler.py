'''
Say that you are a traveler on a 2D grid. You begin in the top-left corner and you goal to to travel to the bottom-right
corner. You may only move down or right
In how many ways can you travel to the goal on a grid with dimension m*n?
Write a function "gridTraveler(m, n)" that calculate this
'''
def gridTraveler(m, n, memo):
    key = str(m) + ", " + str(n)
    if key in memo:
        return memo[key]
    if n == 1 and m == 1:
        return 1;
    if n == 0 or m == 0:
        return 0;
    memo[key] = gridTraveler(m -1,  n, memo) + gridTraveler(m, n -1, memo)
    return memo[key]

m = dict()
print(gridTraveler(18, 18, m))