class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # brute force
        # if not t or not s:
        #     return ""
        # t_counter = Counter(t)
        # n = len(s)
        # min_win = None
        # min_length = float("inf")

        # for i in range(n):
        #     for j in range(i, n):
        #         current_sub = s[i: j + 1]
        #         if not (t_counter - Counter(current_sub)):
        #             if len(current_sub) < min_length:
        #                 min_length = len(current_sub)
        #                 min_win = current_sub
        #             break
        # return min_win if min_win is not None else ""
        
        #optimal
        # Count frequency of characters in t
        tCount = Counter(t)
        # Dictionary to keep count of characters in the current window
        window = {}
        # 'have' tracks how many unique characters meet the required count in the current window
        # 'need' is the total number of unique characters required (from t)
        have, need = 0, len(tCount)
        
        # Result window indices and its length
        res, resLen = [-1, -1], float("inf")
        l = 0  # Left pointer of the window
        
        # Expand the window with the right pointer
        for r, char in enumerate(s):
            # Add one occurrence of the current character to the window
            window[char] = 1 + window.get(char, 0)
            
            # Check if the current character satisfies the count required by tCount
            if char in tCount and window[char] == tCount[char]:
                have += 1
            
            # While current window contains all required characters, try to contract it
            while have == need:
                # Update the result if this window is smaller than the previous best
                if (r - l + 1) < resLen:
                    res, resLen = [l, r], (r - l + 1)
                
                # Remove the leftmost character from the window and move the left pointer
                window[s[l]] -= 1
                # If the removed character is required and its count falls below the target, decrement 'have'
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        
        start, end = res
        # Return the minimum window substring if found; otherwise, return an empty string.
        return s[start: end + 1] if resLen != float("inf") else ""
            
            
            
            

