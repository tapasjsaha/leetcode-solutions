# First Bad Version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
def isBadVersion(version):
    bad_ver = 1  # change as per test case
    if version >= bad_ver:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lv, hv = 1, n
        while lv < hv:
            mv = (lv + hv) // 2
            print("l, m, h = ", lv, mv, hv)
            if isBadVersion(mv):
                hv = mv
            else:
                lv = mv + 1
        return hv


s = Solution()
#print(s.firstBadVersion(n=5))
print(s.firstBadVersion(n=2))
