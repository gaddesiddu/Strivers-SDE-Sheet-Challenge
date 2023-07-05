class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        element=None
        for i in range(n):
            if c==0:
                ele=nums[i]
                c=1
            elif ele==nums[i]:
                c+=1
            else:
                c-=1
        #checking if stored element is majority or not 
        c1=0
        for i in range(n):
            if ele==nums[i]:
                c1+=1
        if c1>(n//2):
            return ele
        return -1