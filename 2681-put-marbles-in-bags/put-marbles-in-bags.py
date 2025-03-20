class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # greedy solution
        # array of partition costs
        partition_costs = sorted(weights[i - 1] + weights[i] for i in range(1, len(weights)))

        # cost if entire array is one partition
        ends = weights[0] + weights[-1]

        if k - 1 <= 0:
            return ends - ends

        min_cost = ends + sum(partition_costs[:(k-1)])
        max_cost = ends + sum(partition_costs[-(k-1):])

        return max_cost - min_cost

        #dp solution does not pass all test cases, time limit exceeded
        # n = len(weights)
        # if k > n:
        #     return 0
        
        # INF = float("inf")

        # dpMin = [[INF]*(k+1) for _ in range(n+1)]
        # dpMax = [[-INF]*(k+1) for _ in range(n+1)]

        # dpMin[0][0], dpMax[0][0] = 0, 0

        # for i in range(1, n + 1):
        #     for p in range(1, min(i, k) + 1):
        #         for m in range(p - 1, i):
        #             cost_sub = weights[m] + weights[i - 1]
        #             if dpMin[m][p-1] != INF:
        #                 dpMin[i][p] = min(dpMin[i][p], dpMin[m][p-1] + cost_sub)
        #             if dpMax[m][p-1] != -INF:
        #                 dpMax[i][p] = max(dpMax[i][p], dpMax[m][p-1] + cost_sub)
        # return dpMax[n][k] - dpMin[n][k]