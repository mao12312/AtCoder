while True:
    nums = list(map(int, input().split()))
    if nums == [0, 0]:
        break
    else:
        nums.sort()
        print(nums[0], nums[1])