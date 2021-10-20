
# Approach 1
# Python Implementation of the approach
import itertools
 
def Sub_Sequences(STR):
    combs = []
    for l in range(1, len(STR)+1):
        combs.append(list(itertools.combinations(STR, l)))
    for c in combs:
        for t in c:
            print (''.join(t), end =' ')
 
# Testing with driver code
if __name__ == '__main__':
    Sub_Sequences('abc')


# Approach 2

# A subsequence is obtained by skipping few indexes in a string
# Lets say we have string s="abc"
# "ac" is a subsequence of "abc" and is obtained by skipping "b" at 1st-index
# we can consider a binary representation equal to length of "abc" (i.e 3) as 101.
# 1 means we take that index and 0 means we ignore that index
# in "101" we take 0th and 2nd indices and skip 1st index as it's "0" in binary form.
# Idea is to generate all bitmasks of length same as the input string.
# Now for a given bitmask, we check all indices from left to right which are "1" and include
# characters at those indices as a part of the new subsequence.

class Solution:
    def print_subsequences(self, S):
        # read length of input string
        input_length = len(S)

        # iterate over all possible binary strings (bitmasks) of length equal to input string length
        for bitmask in range(0, (1 << (input_length))):
            # subsequence formed for current bitmask
            curr_subsequence = ''

            # iterate over all indices of input string
            for index in range(0, input_length):

                # check if current index is set to "1" in current binary string ( current bitmask)
                if (bitmask & (1 << index)) > 0:
                    curr_subsequence += S[index]
            print(curr_subsequence)

# Complexity Analysis

# Time Complexity: O(N * (2 ^ N)), where N is the length of input string.

# Space Complexity: O(2^N) where N is the length of input string, as we are storing all possible subsequences.
