class Solution:
    def largestPalindromic(self, num: str) -> str:
        # counting the number of occurrence of each digit
        count = Counter(num)
        # if the occurrence is multiple of 2, we'll take then in descending order and remove if there any leading zero (0)
        res = "".join(count[i] // 2 * i for i in '9876543210').lstrip("0")
        # taking the max of the odd number(s) of occurrence of digit
        mid = max(count[i]%2 * i for i in count)
        return (res+mid+res[::-1]) or "0"