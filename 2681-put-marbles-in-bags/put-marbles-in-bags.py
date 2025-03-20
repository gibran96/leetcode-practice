class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        partition_costs = sorted(weights[i - 1] + weights[i] for i in range(1, len(weights)))
        ends = weights[0] + weights[-1]
        if k - 1 <= 0:
            return ends - ends
        print(ends, partition_costs)
        min_cost = ends + sum(partition_costs[:(k-1)])
        max_cost = ends + sum(partition_costs[-(k-1):])
        print(min_cost, max_cost)
        return max_cost - min_cost