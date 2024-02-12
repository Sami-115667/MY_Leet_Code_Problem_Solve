class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        intersection = []

        # Iterate through the smaller set to find the intersection
        if len(nums1) <= len(nums2):
            for num in nums1:
                if num in nums2:
                    intersection.append(num)
        else:
            for num in nums2:
                if num in nums1:
                    intersection.append(num)

        return intersection
