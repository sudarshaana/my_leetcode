import sys
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        s1 = {k: v for v, k in enumerate(list1)}
        
        min_sum = 99999
        all_matched = True
        answers = {}
        
        
        for i, l in enumerate(list2):
            if l in s1:
                
                if i+s1[l] == min_sum:
                    answers[min_sum].append(l)
                
                elif i+s1[l] < min_sum:
                    min_sum = i+s1[l]
                    answers[min_sum] = [l]
                
            else:
                all_matched = False
                
        
        return answers[min(answers.keys())]