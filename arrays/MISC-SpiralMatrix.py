import numpy as np
from typing import List

"""
Problem 59. Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]
"""



class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def turn_right(moving_in_row, moving_in_col):
            assert moving_in_col * moving_in_row == 0
            r_m_row = 0
            r_m_col = 0
            if moving_in_col == 1:
                r_m_row = 1
                r_m_col = 0
            elif moving_in_row == 1:
                r_m_row = 0
                r_m_col = -1
            elif moving_in_col == -1:
                r_m_col = 0
                r_m_row = -1
            elif moving_in_row == -1:
                r_m_row = 0
                r_m_col = 1
            return r_m_row, r_m_col

        arr = np.zeros((n,n), dtype=np.int32)
        row = 0
        col = 0
        moving_in_row = 0
        moving_in_col = 1
        # ticks that we need to turn right:
        #   n, n-1, n-1, n-2, n-2, n-3, n-3, ...
        counter_index = 0
        counter_max2 = 1
        counter_movement = 0
        for num in range(1, n**2 + 1):
            arr[row, col] = num
            counter_movement += 1
            if counter_movement == n-counter_index:
                # First, we turn right
                moving_in_row, moving_in_col = turn_right(moving_in_row, moving_in_col)
                # Second, we update counter
                # 1. clear movement counter
                counter_movement = 0
                # 2. update counter_max2
                counter_max2 += 1
                # 3. update counter_index
                if counter_max2 == 2:
                    counter_max2 = 0
                    counter_index += 1
            # Finally, update next_index
            row += moving_in_row
            col += moving_in_col
        return arr.tolist()

            
# Test cases
if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.generateMatrix(n))
