class Solution:
    def maximum69Number (self, num: int) -> int:
        
#         new_num = []
#         for i, n in enumerate(str(num)):
#             if n == '6':
#                 new_num.append('9')
#                 new_num.append(str(num)[i+1:])
#                 break
#             else:
#                 new_num.append(n)
        
#         return int("".join(new_num))

        nums = list(str(num))
    
        for i, cur_num in enumerate(nums):
            if cur_num == '6':
                nums[i] = '9'
                break
                
        return int("".join(nums))