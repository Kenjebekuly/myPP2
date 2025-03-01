import re
def match_p(t):
    p=r'^ab{2,3}$'
    if re.fullmatch(p, t):
        return True
    return False

p=str(input())
print(match_p(p))