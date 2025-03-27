class Solution:
    def minWindow(self, s: str, t: str) -> str:
        win = len(t)
        l, r = 0, 0
        countT = Counter(t)
        res = "*" * 999999
        tCount = Counter(t)
        win = {}
        res, resLen = [-1, -1], float("inf")
        have, need = 0, len(tCount)
        l = 0
        for r in range(len(s)):
            c = s[r]
            win[c] = 1 + win.get(c, 0)

            if c in tCount and win[c] == tCount[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                win[s[l]] -= 1
                if s[l] in tCount and win[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        start, end = res
        return s[start: end + 1] if resLen != float("inf") else ""

            
            
            
            

