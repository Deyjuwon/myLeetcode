def twoSum(nums, target):
    for i in nums:
        print(i)
        for j in nums:
            print(j)
            sumOne = i + j

            if sumOne == target and nums.index(i) != nums.index(j):
                return([nums.index(i), nums.index(j)])




print(twoSum([3, 3], 6))