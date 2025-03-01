import re
def replace_delimiters(t):
    p=r'[,.]'
    return re.sub(p, ':', t)

p=str(input())
print(replace_delimiters(p))