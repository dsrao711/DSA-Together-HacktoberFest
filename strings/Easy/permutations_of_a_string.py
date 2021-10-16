# Link : https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1

# Approach
# To generate permutations of a string, we start with one particular index and try to swap
# this index with other indexes to generate new permutations.
# This swapping is used for all the indices in order to generate all permutations
# Recursion base case occurs when string in consideration reaches length 1.

class Solution:
    def find_permutation(self, S):
        # list to store all permutations
        result = []

        # generator functions to return all possible permutations
        def generate(S, st, en):
            # base case when string to be considered reaches length 1
            if st == en:
                result.append(''.join(S))
            else:
                # try swapping all characters with current index
                for index in range(st, en + 1):
                    # swap current index with other indexes in range [st, en]
                    S[st], S[index] = S[index], S[st]
                    # recursive call for next permutation
                    generate(S, st + 1, en)
                    # revert the previous swapping
                    S[st], S[index] = S[index], S[st]

        # sub-method to generate all permutations
        generate(list(S), 0, len(S) - 1)
        # sort the list of permutations generated
        result.sort()
        return result

# Complexity Analysis

# Time Complexity: O(N * N!), where N is the length of input string.

# Space Complexity: O(N) where N is the length of input string.
