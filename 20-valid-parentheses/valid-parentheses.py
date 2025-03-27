class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        pMap = {"}": "{", ")": "(", "]": "["}
        stack = []
        for c in s:
            if c in pMap:
                if not stack or stack[-1] != pMap[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack
        