import re
def match_p(t):
    p=r'^[a-z]+_[a-z]+$'
    if re.fullmatch(p, t):
        return True
    return False

p=str(input())
print(match_p(p))