'''
Q. Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
'''
# Ans :

def addBinary(a, b):
    # return bin(int(a, 2) + int(b, 2))[2:]
    i = len(a)-1
    j = len(b)-1
    carry = 0
    result = []

    while(i>=0 or j>=0 or carry>0):

        bit1 = int(a[i]) if i >= 0 else 0
        bit2 = int(b[j]) if j >= 0 else 0
        
        current_sum = (bit1 + bit2  + carry)
        result_bit = current_sum % 2
        carry = current_sum // 2

        result.append(str(result_bit))

        i -= 1
        j -= 1
    return "".join(result[::-1])


print(addBinary("11", "1"))
print(addBinary("1010", "1011"))

