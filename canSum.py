# Write a function called "canSum(targetSum, number)" that takes in a targetSum and an array of numbers as arguments.
# The function should return a boolean indicating whether or not it is possible to generate the targetSum using numbers from the array
#  You may use an element of the array as many times as needed
#  You may assume that all input numbers are non-nagative
# For example:   
 #              {8, [2, 3, 5]} => True, because 8 = 2 + 3 + 5
 #              {7, [3, 4, 7]} => True, because 7 = 3 + 4 or 7 = 7
 #              {300, [7, 14]} => False, because impossible 

def canSum(targetSum, numbers, memo):
    if targetSum in memo:
        return memo
    if targetSum == 0:
        return True;
    if targetSum <  0:
        return False;
    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers, memo) == True:
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False
m = dict()

print(canSum(300, [7, 14], m))
print(canSum(8, [2, 3, 5], m))