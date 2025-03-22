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
        q = collections.deque()
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                max_slide.append(nums[q[0]])
                l += 1
            r += 1
        return max_slide

            
