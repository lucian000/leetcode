#
# [401] Binary Watch
# 
# * Easy(44.78172%)
# * Testcase Example: '0'
# * URL: https://leetcode.com/problems/binary-watch
# 
# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
# Each LED represents a zero or one, with the least significant bit on the right.
# 
# For example, the above binary watch reads "3:25".
# 
# Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
# 
# Example:
# Input: n = 1Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
# 
# 
# Note:
# 
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
# 
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        time = [bin(i)[2:].count('1') for i in range(60)]
        ans=[]
        for i in range(max(num-5,0),min(num+1,4)):
            j=num-i
            h=[]
            m=[]
            for ii,cc in enumerate(time[:12]):
                if cc==i:
                    h.append(ii)
                if cc==j:
                    m.append(ii)
            for ii,cc in enumerate(time[12:]):
                if cc==j:
                    m.append(ii+12)
            for hh in h:
                for mm in m:
                    if mm<10:
                        ans.append(str(hh)+':0'+str(mm))
                    else:
                        ans.append(str(hh)+':'+str(mm))
        return ans
