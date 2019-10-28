def binSearch(self,nums, target):
    start = 0
    end = len(nums) - 1
    while start + 1 < end:
        mid = start + (end - start) // 2
        if nums[mid] > target:
            end = mid
        else:
            start = mid

    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    else:
        return -1


# 找旋转数组最小值
def findMin(self, A):
    # write your code here
    start, end = 0, len(A) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if A[mid] < A[end]:
            end = mid
        else:
            start = mid

    if A[start] < A[end]:
        return A[start]
    return A[end]
