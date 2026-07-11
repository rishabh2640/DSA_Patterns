# there are two given strings in a function s & c, c is single character string. we have to return string s while removing the character c from it. If c has length other than 1, then return s.

def del_char(s,c):
    if len(c) == 1:
        return s.replace(c,"")
    else:
        return s

print(del_char("BANANA", "A"))