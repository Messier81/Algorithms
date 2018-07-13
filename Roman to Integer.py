class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        tot = 0
        for c in reversed(s):

            if c == "I":
                tot += 1
            if c == "V":
                tot += 5
            if c == "X":
                tot += 10
            if c == "L":
                tot += 50
            if c == "C":
                tot += 100
            if c == "D":
                tot += 500
            if c == "M":
                tot += 1000

        if 'IV' in s:
            tot -= 2
        if 'IX' in s:
            tot -= 2
        if 'XL' in s:
            tot -= 20
        if 'XC' in s:
            tot -= 20
        if 'CD' in s:
            tot -= 200
        if 'CM' in s:
            tot -= 200
        return tot

Solution.romanToInt("a","VII")