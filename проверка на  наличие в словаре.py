d=[input().lower() for i in range(int(input()))]
l=[input().lower().split() for j in range(int(input()))]
res=set([k for x in l for k in x if k not in d])
[print(m) for m in res]
