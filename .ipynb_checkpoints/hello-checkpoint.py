def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
                
        nums3 = nums1 + nums2  # Combine lists
        nums3.sort()           # Sort the combined list
        i = len(nums3)

        if i == 0:
            return 0.0 # Or raise an error for empty list

        if i%2 == 0:
            # For even length, average of middle two elements
            median = (float(nums3[i//2] + nums3[i//2 - 1]))/2.0
        else:
            # For odd length, the middle element
            median = float(nums3[i//2])

        return median
        

nums1 = [1,2,3]
nums2 = [4,5,6]
print(findMedianSortedArrays(nums1,nums2))