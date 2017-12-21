class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        """
        :Take absolute value to get rid of negative
        """
        x = abs(x)
        if x < 10:
            return True
        
        i = x
        j = 0
        
        while i >= 1:
            i = i / 10
            j += 1
            
        loop_counter = int(j / 2)
        
        print (j)
       

a = Solution()
a.isPalindrome(21712);        