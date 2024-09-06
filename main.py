class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        g=len(nums)+1
        n2=[n for n in range(1,g)]
        return (list(set(n2) - set(nums)))