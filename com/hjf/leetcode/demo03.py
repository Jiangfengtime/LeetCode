def replaceSpaces(S: str, length: int) -> str:
    s1 = ""
    for ele in S[:length]:
        if ele == ' ':
            ele = "%20"
        s1 += ele
    return s1


print(replaceSpaces("               ", 5))

