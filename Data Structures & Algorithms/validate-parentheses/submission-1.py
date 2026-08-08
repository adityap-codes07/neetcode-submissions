class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        box = []
        for i in s:
            if i in bracket:
                if len(box) == 0 or box[-1] != bracket[i]:
                    return False
                box.pop()
            else:
                box.append(i)
        return True if not box else False

