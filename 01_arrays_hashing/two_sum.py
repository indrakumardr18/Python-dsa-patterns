# Two Sum - LeetCode #1
# Pattern: HashMap lookup
def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i
    return []


def two_sum(nums:list[int], target:int) -> list[int]:
    hashmap = {}  # Step 1: Create an empty dictionary to store num:index pairs

    # Step 2: Iterate through nums with index and value
    for i, num in enumerate(nums):
        complement = target - num  # Step 3: Calculate complement
        
        # Step 4: Check if complement exists in hashmap
        if complement in hashmap:
            return [hashmap[complement], i]  # If yes, return indices immediately
        
        # Step 5: Otherwise, store current number with its index in hashmap
        hashmap[num] = i
    
    # Step 6: If no pair found (problem states one solution exists, so usually not reached)
    return []
