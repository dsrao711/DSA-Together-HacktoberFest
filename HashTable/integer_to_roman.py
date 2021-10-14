# Link :  https://leetcode.com/problems/integer-to-roman/

# Approach
# One pattern to notice is that if we consider the list of following numbers
# [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
# we can easily observe that if we take any 2 adjacent elements in above list, for e.g. [100,400]
# all numbers lying in the range [100 - 400] can be formed starting with roman symbol of 100.
# Similarly for range [500,900] all numbers can be formed starting with roman symbol for 500.
# So we try to find for given num, the largest integer in above list which is smaller than or equal to the current num
# once we find that number just append it's roman symbol to result , subtract this number from current num
# and call recursive function to solve for the new number obtained after subtraction.
# Recursion base case occurs when current number is present in the list itself.
# Note: We will always reach the base case :)

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # set of base integers
        base_integers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

        # roman representation for base integers
        base_integers_to_roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

        # recursive method to convert integer to roman representation
        def convert(num):
            # binary search parameters initialization
            low = 0
            high = len(base_integers) - 1
            best_index = high

            # finding the index of largest number smaller than "num" in base_integers list
            while low <= high:
                mid = (low + high) / 2
                if base_integers[mid] <= num:
                    best_index = mid
                    low = mid + 1
                else:
                    high = mid - 1

            # base case when "num" itself is present in the base_integers list
            if base_integers[best_index] == num:
                return base_integers_to_roman[best_index]

            # we recur for new number obtained by subtracting from current "num"
            return base_integers_to_roman[best_index] + convert(num - base_integers[best_index])

        return convert(num)

# Complexity Analysis

# Time Complexity: O(N/M), where N is the input and M is largest number smaller than or equal to N.

# Space Complexity: O(1)
