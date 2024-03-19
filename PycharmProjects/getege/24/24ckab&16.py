f=open("24ckab&16.txt").readline().split("A")
k=[]
for a,b in zip(f,f[1:]):k.append(a+b+"A")
print(max(map(len,k)))