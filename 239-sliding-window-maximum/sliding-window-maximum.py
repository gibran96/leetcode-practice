class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # O(nxk) solution
        # max_slide = []
        # l, r = 0, k - 1
        # while r < len(nums):
        #     win = nums[l: r + 1]
        #     win.sort()
        #     max_slide.append(win[-1])
        #     l += 1
        #     r += 1
        # return max_slide

        dq = collections.deque()
        res = []
        for i, val in enumerate(nums):
            while dq and nums[dq[-1]] <= val:
                dq.pop()
            
            dq.append(i)

            if dq[0] <= i - k:
                dq.popleft()

            if i >= k - 1:
                res.append(nums[dq[0]])
        return res

            



            
