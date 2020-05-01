# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        if isBadVersion(n):
            first_bad = n
        else:
            return 0
        while(start <= end):
            mid = (start + end) // 2
            if isBadVersion(mid):
                first_bad = mid
                end = mid - 1
            else:
                start = mid + 1
        return first_bad