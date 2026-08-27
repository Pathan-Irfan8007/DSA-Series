def isIsomorphic(s, t):
    hash_map = {}
    reverse_map = {}
    for i in range(len(s)):
        if s[i] not in hash_map and t[i] not in reverse_map:
            hash_map[s[i]] = t[i]
            reverse_map[t[i]] = s[i]

        elif s[i] in hash_map and hash_map[s[i]] != t[i]:
            return False
        
        elif t[i] in reverse_map and reverse_map[t[i]] != s[i]:
            return False

    return True


print(isIsomorphic("abb", "eff"))
print(isIsomorphic("f11", "b23"))
print(isIsomorphic("badc", "baba"))

        
