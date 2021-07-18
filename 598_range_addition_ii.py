
from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
        x = m
        y = n
        for a,b in ops :
            x = min(x,a)
            y = min(y,b)


        return  x*y



        
def main():
    
    sol = Solution()
    n = 3
    m = 3
    ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
    

    print(sol.maxCount(n,m,ops))


if __name__ == "__main__":
    # execute only if run as a script
    main()
