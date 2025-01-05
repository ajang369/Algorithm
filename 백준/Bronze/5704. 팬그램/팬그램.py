while 1:
    s = input()
    if s == "*":
        break

    alpa = []
    for i in s:
        if i == " ":
            continue
        if i not in alpa:
            alpa.append(i)

    if len(alpa) == 26:
        print("Y")
    else:
        print("N")