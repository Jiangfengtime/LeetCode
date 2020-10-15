def canPermutePalindrome(s: str) -> bool:
    set1 = set()
    for ele in s:
        if ele in set1:
            set1.remove(ele)
        else:
            set1.add(ele)
    if len(set1) == 0 or len(set1) == 1:
        return True
    else:
        return False


print(canPermutePalindrome("tactcoa"))
