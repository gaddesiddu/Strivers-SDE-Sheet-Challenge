from typing import *

def ncr(n,r):
        
        #n-rows,r-cols
    ans=1
    for i in range(r):
        #r is cols
        ans=ans*(n-i)
        ans=ans//(i+1)
    return ans
class Solution:
    def generate(self, n: int) -> List[List[int]]:
       
        res=[]
        for row in range(1,n+1):
            temp=[]
            for cols in range(1,row+1):
                temp.append(ncr(row-1,cols-1))
                #applying ncr formula so (n-1)C(r-1) 5C3=4*3*2//3*2
            res.append(temp)
        return res
    
    