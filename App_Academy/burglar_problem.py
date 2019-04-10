# Like this https://leetcode.com/problems/house-robber/ except return the solution sets
def rob(nums):
    if not nums: return 0
    # NB: below IS DANGEROUS because then all nested lists have SAME REFERENCE, add to one you change them all.
    # dp_sets = [[]] * (len(nums)+1)
    dp_sets = [[[]] for _ in range(len(nums)+1)]
    dp_sets[1] = [[nums[0]]]
    dp = dp = [0] * (len(nums)+1)
    dp[1] = nums[0]
    # print('nums:' +str(nums)) 
    # print(dp)
    # print(dp_sets)
    for idx in range(2,len(dp)):
        # print(idx)
        dp[idx] = max(dp[idx-1], nums[idx-1]+dp[idx-2])
        prev_house_sets = dp_sets[idx-1]
        take_this_house_sets = [d+[nums[idx-1]] for d in dp_sets[idx-2]]
        if dp[idx-1] == nums[idx-1]+dp[idx-2]:
            # doesn't matter if you take this house or not
            dp_sets[idx] = prev_house_sets + take_this_house_sets
        elif dp[idx] == dp[idx-1]:
            dp_sets[idx] = prev_house_sets
            # print('prev_house_sets: ' + str(prev_house_sets))
        else:
            dp_sets[idx] = take_this_house_sets
            # print('take_this_house_sets: ' + str(take_this_house_sets))
        # print(dp)
        # print(dp_sets)
    return dp_sets[-1]

if __name__ == "__main__":
    print(rob([1, 5, 16, 20, 3, 7, 10, 5, 10, 25, 17])) # 2 sets of 62 should be the answer
    # print(rob([1,5,16,20,3,7,10,5,25,17])) 
