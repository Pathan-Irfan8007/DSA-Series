def frequency(nums):
    freq_dict = {}
    for i in nums:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    return freq_dict

def frequency2(nums):
    freq_dict = {}
    for i in nums:
        freq_dict[i] = freq_dict.get(i, 0)+1
    return freq_dict

print(frequency(["a","b","c","d","b","c","a","b","c"]))
print(frequency2(["a","b","c","d","b","c","a","b","c"]))