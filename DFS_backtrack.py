# 组合之和问题可以看出来DFS回溯其实是有套路的
class Solution:
    def combinationSum(self, candidates, target):
        candidates = sorted(list(set(candidates)))
        results = []
        self.dfs(candidates, target, 0, [], results)
        return results

    def dfs(self, candidates, target, start, combination, results):
        if target < 0:
            return

        if target == 0:
            # deepcooy
            return results.append(list(combination))

        for i in range(start, len(candidates)):
            # [2] => [2,2]
            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, combination, results)
            # [2,2] => [2]
            combination.pop()