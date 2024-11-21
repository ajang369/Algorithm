import sys


input = sys.stdin.readline
n= int(input())
li = []
temp=[]
name=set()
for _ in range(n):
    temp = list(input().strip().split())
    if temp[1]=='enter':
        name.add(temp[0])
    if temp[1]=='leave':
        name.discard(temp[0])
li=list(name)
li.sort()
li.reverse()
for i in li:
    print(i)