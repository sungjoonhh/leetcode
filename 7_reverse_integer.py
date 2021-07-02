# Definition for singly-linked list.
class Solution:
    def reverse(self, x: int) -> int:
        num = 0        
        if x>=0 :
            while x > 0:
                
                num = int(num*10) + int((x%10))
                x = int(x/10)
            return  0 if num > int(pow(2,31)) else num
        else :
            x = x*-1
            while x > 0:
                
                num = int(num*10) + int((x%10))
                x = int(x/10)
            return 0 if num <pow(2,31) else num*-1

def main():
    sol = Solution()
    print(sol.reverse(1534236469))
    print(pow(2,31))


if __name__ == "__main__":
    # execute only if run as a script
    main()