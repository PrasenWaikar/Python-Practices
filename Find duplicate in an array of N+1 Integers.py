def find_duplicate(nums):
    # Phase 1: Find intersection point in the cycle
    tortoise = nums[0]
    hare = nums[0]
    
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    
    # Phase 2: Find the entrance to the cycle
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
    
    return tortoise

# Example usage
nums = [3, 1, 3, 4, 2]
print(find_duplicate(nums))  # Output: 3
