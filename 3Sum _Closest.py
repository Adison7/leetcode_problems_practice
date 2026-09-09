def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closest = nums[0] + nums[1] + nums[2]  # initial guess

    for i in range(n - 2):
        # optional optimization: skip duplicate anchors
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]

            if curr_sum == target:
                return curr_sum  # exact match, can't do better

            if abs(curr_sum - target) < abs(closest - target):
                closest = curr_sum

            if curr_sum < target:
                left += 1
            else:
                right -= 1

    return closest