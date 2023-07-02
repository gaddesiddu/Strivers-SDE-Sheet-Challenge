class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        
        
        n = len(A)
        c=[0]*(n+1)
        for i in range(n):
            c[A[i]]+=1
            
        repeat, miss = -1, -1
        for i in range(1,n+1):
            if c[i]==2:
                repeat=i
            elif c[i]==0:
                miss=i
        
            if repeat != -1 and miss != -1:
                break
        return [repeat, miss]



