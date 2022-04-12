https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1,numRows):
            firstHalf = [1]
            mid = (i+1)//2
            secondHalf = []
            if (i+1)%2==0:
                for k in range(1,mid):
                    firstHalf.append(ans[i-1][k-1]+ans[i-1][k])
                secondHalf = firstHalf[::-1]
            else:
                for k in range(1,mid+1):
                    firstHalf.append(ans[i-1][k-1]+ans[i-1][k])
                secondHalf = firstHalf[::-1]
                secondHalf = secondHalf[1:]
            ans.append(firstHalf+secondHalf)
        return ans