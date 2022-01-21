class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # Base case
        if x < 2:     
            return x
 
        # to store floor of `sqrt(x)`
        result = 0
        
        # the square root of `x` cannot be more than x/2 for `x` > 1
        start = 1
        end = x // 2

        while start <= end:

            # find the middle element
            mid = (start + end) // 2
            sqr = mid*mid
            print(mid)

            # return `mid` if `x` is a perfect square
            if sqr == x:
                print("Mid found")
                print(sqr)
                return mid

            # if `mid×mid` is less than `x`
            elif sqr < x:
                # discard left search space
                start = mid + 1
                # update result
                result = mid
                print("Lesser")
 
            # if `mid×mid` is more than `x`
            else:
                # discard the right search space
                end = mid - 1

        # return result
        return result