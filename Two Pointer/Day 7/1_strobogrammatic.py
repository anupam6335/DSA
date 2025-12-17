def is_strobogrammatic(nums: str) -> bool:
    mapping = {
        '0' : '0',
        '1' : '1',
        '6' : '9',
        '8' : '8',
        '9' : '6',
    }

    i = 0
    j = len(nums) - 1

    while i <= j:
        if nums[i] not in mapping:
            return False
        elif mapping[nums[i]] != nums[j]:
            return False 
        i += 1
        j -= 1
    return True 

print(is_strobogrammatic('16891'))
