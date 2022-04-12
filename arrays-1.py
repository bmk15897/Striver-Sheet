# https://leetcode.com/problems/set-matrix-zeroes/



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        z = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    z = z + [(i,j)]
        for k in z:
            for a in range(m):
                matrix[a][k[1]]=0
            for a in range(n):
                matrix[k[0]][a]=0
            
                