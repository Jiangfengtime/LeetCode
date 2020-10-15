def compressString(S: str) -> str:
    i = j = 0
    len1 = len(S)
    s1 = ""
    count = 0
    while j < len1:
        if S[i] == S[j]:
            j += 1
            count += 1
        else:
            i = j
            count = 0
        if count == 0:
            s1 = s1 + S[i] * count

    len2 = len(s1)
    if len1 > len2:
        return s1
    else:
        return S


print(compressString("abbbbccd"))
