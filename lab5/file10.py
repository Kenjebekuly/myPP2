import re
def camel_to_snake(t):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', t).lower()

p=str(input())
print(camel_to_snake(p))