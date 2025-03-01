import re
def splitt(t):
    return re.findall(r'[^A-Z]+|[A-Z][^A-Z]*', t)

p=str(input())
print(splitt(p))