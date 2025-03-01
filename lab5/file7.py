import re
def snake_to_camel(t):
    return ''.join(w.capitalize() if i>0 else w for i, w in enumerate(t.split('_')))

p=str(input())
print(snake_to_camel(p))