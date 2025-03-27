class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pairs = [(p, s) for p, s in zip(position, speed)]
        # pairs.sort()
        # print(pairs)
        # fleets = 0
        # stack = []
        
        # for p, s in sorted(pairs)[::-1]:
        #     t = (target - p) / s
        #     stack.append(t)
        #     if len(stack) >= 2 and stack[-1] <= stack[-2]:
        #         stack.pop()
        # return len(stack)

        #greedy
        pairs = sorted(zip(position, speed), reverse=True)
        fleets = 0
        cur_time = 0.0

        for p, s in pairs:
            t = (target - p) / s

            if t > cur_time:
                fleets += 1
                cur_time = t
        return fleets

            