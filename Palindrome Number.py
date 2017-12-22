#Determine whether an integer is a palindrome. Do this without extra space.
class Solution(object):
    def isPalindrome(self, x):
        #If x is negative, it is not a palindrome..
        #If x is less than 9, it is a plindrome.
        #If x ends in 0, then if x is not 0, then it is not a palindrome.
        if (x < 0 or ((x % 10 == 0) and (x != 0))): 
            return False
        elif (x >=0 and x <= 9):
            return True
        else:
            num = 0
            while x > num:
                num = (num * 10) + int(x % 10)
                x = int(x / 10)
            return x == num or x == num / 10

a = Solution()
print(a.isPalindrome(57075))          