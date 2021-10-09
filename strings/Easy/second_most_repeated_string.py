#Link to the problem : https://practice.geeksforgeeks.org/problems/second-most-repeated-string-in-a-sequence0534/1


class Solution:
    def secFrequent(self, arr, n):
        
        #list to store count of elements 
        elem_count = []

        #dictionary to store elements with occurences
        d = {}
        for i in arr:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
            if arr.count(i) not in elem_count:
                elem_count.append(arr.count(i))

        #sorting the element count array in reverse orderr
        elem_count.sort(reverse = True)

        #element at index 1 is the count of occurence of second most repeated element
        second_high = elem_count[1]
        
        for key in d:
            
            #traversing the dictionary to get the element with second most occurence
            if d[key] == second_high:
                return key

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input().strip())
        arr = input().strip().split(" ")
        ob = Solution()
        ans = ob.secFrequent(arr, n)
        print(ans)

#Time Complexity : O(n)
