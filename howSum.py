'''
Write a function called "howSum(targetSum, number)" that takes in a targetSum and an array of numbers as arguments.

The function should return an array containing any combination of elements that add 
up to exactly the targetSum. If there is no combination that adds to the targetSum, then return null.

If there are multiple combinations possible, you may return any single one
'''

def howSum(targetSum, numbers, memo):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None;
    for num in numbers:
        remainder = targetSum - num;
        remainderResult =  howSum(remainder, numbers, memo)
        if remainderResult != None:
            remainderResult = remainderResult + [num]
            memo[targetSum] = remainderResult
            return memo[targetSum]
    
    memo[targetSum] = None
    return None

m = dict()
print(howSum(7, [2, 3], m))
m = dict()
print(howSum(8, [5, 3, 2], m))
m = dict()
print(howSum(300, [7, 14], m))