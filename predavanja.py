"""
ime=input("Zdravo, kako se zoves?")
s="Zdravo " + ime + ", koliko imas godina?"
drugis=f"Zdravo {ime}, koliko imas godina?"
godine=int(input(s))
print(f"za deset godina ces imati {godine+10} godina")
m=int(input())
m%=(24*60)
print(f"{m//60}h {m%60}min")
b=int(input())
if b%2==0:print("paran")
else:print("neparan")
poena=int(input())
l=[[0,20],[21,40],[41,60],[61,80],[81,100]]
for i in range(len(l)):
    if poena>=l[i][0] and poena<=l[i][1]:
        print(f"To je {i+1}")
if poena>100:
    print("VECE OD 100%")"""
l=list(map(int,input().split()))
print(*l)
maxsto=0
minsta=0
start=0
stop=0
for i in range(1,len(l)):
    if l[i]>l[i-1]:
        stop=i
        continue
    else:
        if maxsto-minsta+1<stop-start+1:
            maxsto=stop
            minsta=start
        start=i
        stop=i
        leng=1
        continue
if maxsto-minsta+1<stop-start+1:
    maxsto=stop
    minsta=start
print(*l[minsta:maxsto+1])