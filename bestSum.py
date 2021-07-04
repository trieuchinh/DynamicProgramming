'''
Write a function called "besSm(targetSum, number)" that takes in a targetSum and an array of numbers as arguments.

The function should return an array containing the shortest combination of numbers that add up to exactly the targetSum.

If there is a tie for the shortest combination, you may return any one of the shortest.
'''

def bestSum(targetSum, numbers, memo):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None;

    shortestCombination =  None
    
    for num in numbers:
        remainder = targetSum - num;
        if remainder >= 0:
            remainderResult =  bestSum(remainder, numbers, memo)
            if remainderResult != None:
                remainderResult = remainderResult + [num]
                if shortestCombination == None or len(shortestCombination) > len(remainderResult):
                    shortestCombination =  remainderResult

    memo[targetSum] = shortestCombination
    return shortestCombination

m = dict()
print(bestSum(7, [5, 3, 7], m))
m = dict()
print(bestSum(8, [5, 3, 2], m))
m = dict()
print(bestSum(8, [1, 4, 5], m))
print(bestSum(100, [1, 2, 5 , 25], m))