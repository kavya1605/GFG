class Solution:
    def checkStatus(self, a, b, flag):
        if not flag:
            # exactly one is non-negative
            return (a >= 0 and b < 0) or (a < 0 and b >= 0)
        else:
            # both are negative
            return a < 0 and b < 0
