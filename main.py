from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
  
    num_indices = {}
    
    for index, num in enumerate(nums):
       
        complement = target - num
        if complement in num_indices:
       
            return [num_indices[complement], index]
        
   
        num_indices[num] = index
    

    return []

#text case
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(twoSum([3, 3], 6))          # Output: [0, 1]
