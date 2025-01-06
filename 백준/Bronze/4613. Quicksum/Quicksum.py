while 1:
    s = input()
    if s == '#':
        break

    quicksum = 0

    for i in range(len(s)):
        if s[i] == " ":
            continue
        quicksum += (ord(s[i])-64) * (i+1)
    print(quicksum)