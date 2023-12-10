"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

DONE: 12/9/23

Axiom: sliding window can help you find an optimized contiguous subarray which satisfies some condition. 

Intuition: 
    1. Open your array up
    2. If you haven't hit the end, keep going. 
    3. Once you fulfill the target, slide the array up.
"""
class SlidingWindow:
    def __init__(self, s, t):
        print(s, t)
        self.targetCharacters = {} 
        for character in t: 
            if character not in self.targetCharacters.keys():
                self.targetCharacters[character] = 1 
            else: 
                self.targetCharacters[character] += 1 

        self.searchString = s 
        self.start, self.end = 0, 0
        self.length = 0

        self.bestStart, self.bestEnd = -1, -1
        self.bestLength = float('infinity')

    def solve(self): 
        self.printCurrent()
        while self.end < len(self.searchString):
            self.incrementWindow()
            self.printCurrent()
            while self.isWindowSatisfied():
                self.storeBest()
                self.decrementWindow()
                self.printCurrent()
        return self.searchString[self.bestStart:self.bestEnd]

    def printCurrent(self):
        print("{}, {}, {}".format((self.start, self.end), self.searchString[self.start: self.end], self.targetCharacters))

    def storeBest(self):
        if self.length < self.bestLength:
            self.bestLength = self.length
            self.bestStart = self.start 
            self.bestEnd = self.end 

    def isWindowSatisfied(self): 
        for value in list(self.targetCharacters.values()):
            if value > 0: 
                return False 
        return True 

    def incrementWindow(self):
        self.end += 1
        self.length += 1
        new = self.searchString[self.end - 1]
        if new in list(self.targetCharacters.keys()):
            self.targetCharacters[new] -= 1

    def decrementWindow(self):
        old = self.searchString[self.start] 
        if old in list(self.targetCharacters.keys()): 
            self.targetCharacters[old] += 1
        self.start += 1 
        self.length -= 1

    def windowIsSatisfied(self):
        for count in list(self.targetCharacters.values()): 
            if count > 0:
                return False 
        else:
            return True 



inputStringOne = "ADOBECODEBANC"
requiredChars = "ABC"
solutionClass = SlidingWindow(inputStringOne, requiredChars)
print(solutionClass.solve())

