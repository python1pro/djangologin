class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        key_index = {'type': 0, 'color': 1, 'name': 2}
        index = key_index[ruleKey]

        # Count items that match the rule
        count = 0
        for item in items:
            if item[index] == ruleValue:
                count += 1
                
        return count
    
solution = Solution()
items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver")
print(countMatches)
































# n = 5
# for i in range(1, n):
#     k = n - i
#     for j in range(1, (n*2-1)):
#         if j >= i and j < n+n-1 -i:
#             print(k, end='')
#         else:
#             print(' ', end='')

#     print()


# for i in range(2, n):
#     for j in range(1, (n*2-1 +1)):
#         if j >= n- i and j <= n+i -2:
#             print(i, end='')
#         else:
#             print(' ', end='')

#     print()



















# n = 5
# for i in range(1, n+1):
#     k = i 
#     for j in range(1, n*2-1 +1):
#         if j >= n+1 - i and j <= (n+1 +i-2):
#             if j < n+1 -1: 
#                 print(k, end='')
#                 k -= 1
#             else:
#                 print(k, end='')
#                 k += 1
#         else:
#             print(' ', end='')
#     print()













        # if j >= i:
        #     print('*', end='')
        # else:
        #     print(' ', end='')
    
        
