class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        num = sorted(set(nums))


        num1 = 0
        num2 = 0

        for i, n in enumerate(num):
            currentEarn = n*count[n]

            if n > 0 and n == num[i-1]+1:
                temp = max(num2, num1+currentEarn)
                num1 = num2
                num2 = temp

            else:
                temp = num2+currentEarn
                num1 = num2
                num2 = temp

        return num2