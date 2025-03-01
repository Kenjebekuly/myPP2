import re
def inserts(t):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', t)

p=str(input())
print(inserts(p))