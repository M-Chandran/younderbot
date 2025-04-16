def largest(nums):
    if len(nums) < 2:
        return None 
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second
numbers = [10, 20, 4, 45, 99]
print("Second largest number is:", largest(numbers))
