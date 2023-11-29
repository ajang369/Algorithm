pipe = input()
stack = []
cnt = []

for i in range(len(pipe)):
    if pipe[i] == '(':
        stack.append('(')
    else:
        if pipe[i-1] == '(':
            stack.pop()
            cnt.append(len(stack))
        else:
            stack.pop()
            cnt.append(1)
print(sum(cnt))