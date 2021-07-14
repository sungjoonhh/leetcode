from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        import copy
        retVal = []
    
        def combination(idx,sum,candidates,target,arr):
                    if idx ==len(candidates) : 
                        return 
                    sum = sum + candidates[idx]
                    arr.append(candidates[idx])
                    print(arr)

                    if sum > target: 
                        return


                    elif sum == target :
                        # print(arr)
                        retVal.append(copy.deepcopy(arr))
                        return arr
                    
                    for i in range(idx,len(candidates)):
                        combination(i,sum,candidates,target,arr)
                        arr.pop(len(arr)-1)
            

        for idx,value in enumerate(candidates) :
            print(idx, value)

            combination(idx,0,candidates,target,[])

        return retVal



                
            



        
def main():
    
    sol = Solution()
    candidates = [2,3,6,7]
    target = 7
    
    print(sol.combinationSum(candidates,target))


    


if __name__ == "__main__":
    # execute only if run as a script
    main()
