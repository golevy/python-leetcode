import time
import copy
from typing import List


class SolutionA:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0
        slow = 0
        size = len(nums)
        while fast < size:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


class SolutionB:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, l = 0, len(nums)
        while i < l:
            if nums[i] == val:
                for j in range(i + 1, l):
                    nums[j - 1] = nums[j]
                l -= 1
                i -= 1
            i += 1
        return l


class SolutionC:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            while left <= right and nums[left] != val:
                left += 1
            while left <= right and nums[right] == val:
                right -= 1
            if left < right:
                nums[left] = nums[right]
                left += 1
                right -= 1
        return left


def test_solution(solution, nums, val):
    nums_copy = copy.deepcopy(nums)
    start_time = time.time()
    k = solution.removeElement(nums_copy, val)
    end_time = time.time()
    print(
        f"Updated Array: {nums_copy[:k]}, New Length: {k}, Execution Time: {end_time - start_time:.6f} seconds"
    )
    return k, nums_copy


nums1 = [3, 2, 2, 3]
val1 = 3
expectedNums1 = [2, 2]

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
expectedNums2 = [0, 1, 4, 0, 3]

solutionA = SolutionA()
solutionB = SolutionB()
solutionC = SolutionC()

print("Testing SolutionA: ")
k1, updated_nums1 = test_solution(solutionA, nums1, val1)
assert k1 == len(expectedNums1)
assert sorted(updated_nums1[:k1]) == sorted(expectedNums1)

k2, updated_nums2 = test_solution(solutionA, nums2, val2)
assert k2 == len(expectedNums2)
assert sorted(updated_nums2[:k2]) == sorted(expectedNums2)

print("Testing SolutionB: ")
k1, updated_nums1 = test_solution(solutionB, nums1, val1)
assert k1 == len(expectedNums1)
assert sorted(updated_nums1[:k1]) == sorted(expectedNums1)

k2, updated_nums2 = test_solution(solutionB, nums2, val2)
assert k2 == len(expectedNums2)
assert sorted(updated_nums2[:k2]) == sorted(expectedNums2)

print("Testing SolutionC: ")
k1, updated_nums1 = test_solution(solutionC, nums1, val1)
assert k1 == len(expectedNums1)
assert sorted(updated_nums1[:k1]) == sorted(expectedNums1)

k2, updated_nums2 = test_solution(solutionC, nums2, val2)
assert k2 == len(expectedNums2)
assert sorted(updated_nums2[:k2]) == sorted(expectedNums2)
