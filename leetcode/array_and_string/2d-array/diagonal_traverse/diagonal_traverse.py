"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order.
Example:
Input:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Output: [1, 2, 4, 7, 5, 3, 6, 8, 9]
"""
from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        moveDown = 0
        result = []
        m = len(matrix)
        n = len(matrix[0])
        for x in range(n + m - 1):
            if moveDown % 2:
                for j in range(min(x, n - 1), max(x - m, -1), -1):
                    result.append(matrix[x-j][j])
            else:
                for i in range(min(x, m - 1), max(x - n, -1), -1):
                    result.append(matrix[i][x-i])
            moveDown += 1
        return result


if __name__ == "__main__":
    with open("input.txt") as file:
        nums = eval(file.read().strip())

    s = Solution().findDiagonalOrder(nums)
    print(s)
