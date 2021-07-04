'''
Write a function "canConstruct(target, wordBank)" that accepts a target string and an array of strings.

The function should return a boolean indicating whether or not the "target" can be constructed by concatenating elements of the "wordBank" array.

You may resuse elements of "wordBank" as many times as needed.
'''

def canConstruct(target, wordBank, memo):
    if target in memo:
        return memo[target]
    if target =="":
        return True
    
    for word in wordBank:
        if target.find(word) == 0:
            suffix =  target[len(word):len(target)]
            if canConstruct(suffix, wordBank, memo) == True:
                memo[target] = True;
                return True
    memo[target] = False;
    return False            
    
m = dict()
print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"], m)) # TRUE
m = dict()
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], m)) # FALSE
m = dict()
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], m)) # TRUE
m = dict()
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
    ["e", 
        "eee", 
            "eeeee", 
                "eeeee", "eeeeeeeeeeeeeeeeeeee"], m)) # FALSE
    