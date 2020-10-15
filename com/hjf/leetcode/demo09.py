def isFlipedString(s1: str, s2: str) -> bool:
    if len(s1) == len(s2) and (s1 + s1).find(s2) != -1:
        return True
    else:
        return False


print(isFlipedString())
