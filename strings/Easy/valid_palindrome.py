result = ''
for i in s:
    if i.lower().isalnum():
        result += i.lower()
return result == result[::-1]
