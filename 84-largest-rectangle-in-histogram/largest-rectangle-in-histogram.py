class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # brute force
        # n = len(heights)
        # max_area = 0
        # for i in range(n):
        #     cur_height = heights[i]
        #     left = i
        #     while left > 0 and heights[left] >= cur_height:
        #         left -= 1
            
        #     right = i
        #     while right < n and heights[right] >= cur_height:
        #         right += 1
            
        #     width = right - left - 1
        #     area = cur_height * width
        #     max_area = max(max_area, area)
        # return max_area

        # stack solution
        max_area = 0
        n = len(heights)
        stack = []

        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] > heights[i]):
                cur_height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, cur_height * width)
            stack.append(i)
        return max_area
 