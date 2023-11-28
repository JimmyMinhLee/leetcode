"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""
class Problem:
    def __init__(self):
        return 

"""
DONE: 11/27/23 
Intuition: 
    While a human can immediately look at [5, 10] and target 50 and say 5 coins, 
    that ignores the actual thought process that occurs. 

    It might actually seem more intuitive to do that, but that's not helpful for a computer. 

    What a human really does is this: 
        I know that I have a 10 and a 5 cent coin. 
        To get to 50, I need to see the minimum number of coins it'd take to make 
            45 and 40, respectively. 
        In this case, we know that 45 takes (4 10's and 1 5), so 5 coins. 
                      we know that 40 takes (4 10's) so 4 coins. 
        To round out the 45 coin case, we add another 5 cent coin and, 
        to round out the 40 coin case, we add another 10 cent coin. 

        Thus, we have: 6 coins (45c) + 1 (5c) 
                  and: 5 coins (40c) + 1 (10c) 

        Then, we take that minimum and store it into our brain somewhere. 

Explicitly: 
    for coin in coins: 
        previous_amt = target - coin 
        self.mem[target] = min(self.mem[target], self.mem[previous_amt] + 1)
"""
class DP:
    def __init__(self, coins, target):
        self.coins = coins 
        self.target = target 
        self.mem = {0: 0} 

    def solve(self): 
        for current_target in range(self.target + 1): 
            current_target_coins = self.mem.get(current_target, 999999)
            current_best = current_target_coins 
            for coin in self.coins: 
                sub_target = current_target - coin 
                sub_target_coins = self.mem.get(sub_target, 999999)
                current_best = min(current_best, sub_target_coins + 1)
            self.mem[current_target] = current_best 

    def get_answer(self):
        answer = self.mem.get(self.target, -1)
        if answer == 999999:
            return - 1
        return answer 

test_coins = [10, 5]
test_amount = 35

solution = DP(test_coins, test_amount)
solution.solve()
print(solution.get_answer())
