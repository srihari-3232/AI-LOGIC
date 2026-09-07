s = input()
longest = 0
for i in range(len(s)):
    temp = ""
    for j in range(i, len(s)):
        if s[j] in temp:
            break
        temp = temp + s[j]
        if len(temp) > longest:
            longest = len(temp)
print(longest)