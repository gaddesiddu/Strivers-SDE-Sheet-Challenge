class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        arr.sort()
        n=len(arr)
        res=[]
        for i in range(n):
            if len(res)==0 or arr[i][0]>res[-1][1]:
                res.append(arr[i])
            else:
                res[-1][1]=max(res[-1][1],arr[i][1])
        return res
        