class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_arr = sorted(nums1 + nums2)
        n = len(merged_arr)

        if n % 2 == 0:
            print(merged_arr)
            print(int((n/2) - 1))
            print(int((n/2) + 1))
            return (merged_arr[int((n/2) - 1)] + merged_arr[int((n/2))]) / 2
        else:
            return merged_arr[n // 2]
        
        