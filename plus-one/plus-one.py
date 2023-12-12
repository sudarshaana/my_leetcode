class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
#         number = "".join(str(i) for i in digits)
        
#         number = int(number)+1
#         number_str = str(number)
        
#         return [int(d) for d in number_str]

#         carry = 1
#         for i in range(len(digits)-1, -1, -1):
            
#             d = digits[i]
#             res = d+carry
#             # print(i, d, res)

#             if res>9:
#                 carry = 1
#                 digits[i] = int(str(res)[-1])
#                 # print(int(str(res)[-1]))
#             else:
#                 digits[i] = res
#                 carry = 0
                
#         if carry ==1:
#             digits.insert(0, 1)
        
#         return digits
            
            n = len(digits)
    
            # Traverse the array from right to left
            for i in range(n - 1, -1, -1):
                # If digit is 9, change it to 0
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    # If not 9, increment it by 1 and return the array
                    digits[i] += 1
                    return digits

            # Special case when all digits are 9
            # Insert a 1 at the beginning of the array
            return [1] + digits