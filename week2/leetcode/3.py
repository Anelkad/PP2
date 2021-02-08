def numIdenticalPairs(nums):
    cnt = 0
    for i in range (0, len(nums)-1):
        for j in range (i+1, len(nums)):
            if nums[i] == nums[j] and i < j:
                cnt += 1
    return cnt
print(numIdenticalPairs([1,1,1,1]))