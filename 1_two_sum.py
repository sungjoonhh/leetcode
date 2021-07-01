class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                temp = nums[i] + nums[j]
                if temp == target:
                    return [i, j]



def main():
    sol = Solution()
    nums = [2,7,11,15]
    target = 9
    output = sol.twoSum(nums,target)
    print(output)
    # output = [0,1]

    


if __name__ == "__main__":
    # execute only if run as a script
    main()