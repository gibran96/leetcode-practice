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

        max_slide = []
        dq = collections.deque()
        l = r = 0
        while r < len(nums):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            if l > dq[0]:
                dq.popleft()
            
            if (r + 1) >= k:
                max_slide.append(nums[dq[0]])
                l += 1            
            r+= 1
        return max_slide
