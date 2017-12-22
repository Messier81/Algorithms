class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor_xy = x ^ y
        count = 0
        for _ in range(32):
        	count += xor_xy & 1
        	xor_xy =  xor_xy >> 1
        return count