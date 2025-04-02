class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # O(nlogn) solution
        # merged_arr = sorted(nums1 + nums2)
        # n = len(merged_arr)

        # if n % 2 == 0:
        #     return (merged_arr[int((n/2) - 1)] + merged_arr[int((n/2))]) / 2
        # else:
        #     return merged_arr[n // 2]
        
        # merge the 2 arrays
        m_arr = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                m_arr.append(nums1[i])
                i += 1
            else:
                m_arr.append(nums2[j])
                j += 1
        
        if i < len(nums1):
            m_arr.extend(nums1[i:])
        if j < len(nums2):
            m_arr.extend(nums2[j:])

        print(m_arr)
        
        n = len(m_arr)
        
        if n % 2 == 0:
            return (m_arr[int((n/2) - 1)] + m_arr[int((n/2))]) / 2
        else:
            return m_arr[n // 2]