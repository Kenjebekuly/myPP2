def permute_string (string, answer):
     for i in range(len(string)):
         ch = string[i]
         left_substr = string[0:i]
         right_substr = string[i + 1:]
         rest = left_substr + right_substr
         permute_string(rest, answer + ch)