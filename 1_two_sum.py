class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                temp = nums[i] + nums[j]
                if temp == target:
                    return [i, j]



    def twoSum2(self, nums, target):
        vals = []
        for i in range(len(nums)):
            if nums[i] in vals:
                return [vals.index(nums[i]), i]
            vals.append(target - nums[i])    


    def BestCase(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i

def main():
    sol = Solution()
    nums = [2,11,15,7]
    target = 9
    output = sol.BestCase(nums,target)
    print(output)
    # output = [0,1]

    


if __name__ == "__main__":
    # execute only if run as a script
    main()