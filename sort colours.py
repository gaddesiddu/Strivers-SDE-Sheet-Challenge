class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cnt_0=0
        cnt_1=0
        cnt_2=0
        for i in nums:
            if i==0:
                cnt_0+=1
            elif i==1:
                cnt_1+=1
            else:
                cnt_2+=1
        for i in range(cnt_0):
            nums[i]=0
        for i in range(cnt_0, cnt_0+cnt_1):
            nums[i]=1
        for i in range(cnt_0+cnt_1,cnt_0+cnt_1+cnt_2):
            nums[i]=2
    
        """
        Do not return anything, modify nums in-place instead.
        """