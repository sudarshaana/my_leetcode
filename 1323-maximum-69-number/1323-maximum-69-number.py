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

#         nums = list(str(num))
    
#         for i, cur_num in enumerate(nums):
#             if cur_num == '6':
#                 nums[i] = '9'
#                 break
                
#         return int("".join(nums))

        #return int(str(num).replace("6", "9", 1))
    
        
        current_digit = 0
        first_index_six = -1
        num_cp = num
        
        while num_cp:
            if num_cp %10 == 6:
                first_index_six = current_digit
            
            num_cp //= 10
            current_digit += 1
        
        return num if first_index_six == -1 else num + 3* 10**first_index_six